#!/usr/bin/env python3
"""Extract public web pages through self-hosted Firecrawl with Crawl4AI fallback."""

from __future__ import annotations

import argparse
import ipaddress
import json
import os
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable, Mapping


DEFAULT_CONFIG_PATH = Path.home() / ".config" / "local-web-extract" / "config.env"
DEFAULT_FIRECRAWL_URL = "http://127.0.0.1:8081"
DEFAULT_TIMEOUT_SECONDS = 60.0
DEFAULT_MIN_CHARS = 80
DEFAULT_MAX_CHARS = 50_000


class ExtractionError(RuntimeError):
    """A provider could not return usable content."""


@dataclass
class ExtractionResult:
    requested_url: str
    final_url: str
    provider: str
    content: str
    title: str | None = None
    content_type: str | None = None
    attempted: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    truncated: bool = False


def parse_env_text(text: str) -> dict[str, str]:
    """Parse simple KEY=VALUE or KEY: VALUE files without executing them."""
    values: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        separator = "=" if "=" in line else ":" if ":" in line else None
        if separator is None:
            continue
        key, value = line.split(separator, 1)
        key = key.strip()
        value = value.strip()
        if not key.replace("_", "").isalnum() or not key[0].isalpha():
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key] = value
    return values


def read_env_file(path: Path) -> dict[str, str]:
    try:
        return parse_env_text(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except OSError as exc:
        raise ExtractionError(f"cannot read environment file {path}: {exc}") from exc


def load_settings(config_path: Path = DEFAULT_CONFIG_PATH) -> dict[str, str]:
    settings = read_env_file(config_path)
    settings.update({key: value for key, value in os.environ.items() if value})
    token_file = settings.get("CRAWL4AI_ENV_FILE")
    if token_file and "CRAWL4AI_API_TOKEN" not in settings:
        settings.update(
            {
                key: value
                for key, value in read_env_file(Path(token_file).expanduser()).items()
                if key not in settings
            }
        )
    return settings


def validate_public_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("URL scheme must be http or https")
    if not parsed.hostname:
        raise ValueError("URL must include a hostname")
    try:
        addresses = {item[4][0] for item in socket.getaddrinfo(parsed.hostname, parsed.port)}
    except socket.gaierror as exc:
        raise ValueError(f"hostname did not resolve: {parsed.hostname}") from exc
    if not addresses:
        raise ValueError(f"hostname did not resolve: {parsed.hostname}")
    for address in addresses:
        ip = ipaddress.ip_address(address)
        if not ip.is_global:
            raise ValueError(f"URL resolves to a private or reserved address: {address}")
    return url


def _post_json(
    endpoint: str,
    payload: Mapping[str, Any],
    *,
    headers: Mapping[str, str] | None = None,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
) -> Any:
    request_headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if headers:
        request_headers.update(headers)
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers=request_headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read(500).decode("utf-8", errors="replace").strip()
        suffix = f": {detail}" if detail else ""
        raise ExtractionError(f"HTTP {exc.code}{suffix}") from exc
    except urllib.error.URLError as exc:
        raise ExtractionError(f"request failed: {exc.reason}") from exc
    except (TimeoutError, json.JSONDecodeError) as exc:
        raise ExtractionError(str(exc)) from exc


def _usable_content(value: Any, provider: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ExtractionError(f"{provider} response missing markdown")
    return value.strip()


def parse_firecrawl_response(requested_url: str, data: Any) -> ExtractionResult:
    if not isinstance(data, dict):
        raise ExtractionError("invalid firecrawl response")
    if data.get("success") is False:
        raise ExtractionError(str(data.get("error") or "firecrawl reported failure"))
    payload = data.get("data") if isinstance(data.get("data"), dict) else data
    assert isinstance(payload, dict)
    content = _usable_content(payload.get("markdown"), "firecrawl")
    metadata_value = payload.get("metadata")
    metadata: dict[str, Any] = metadata_value if isinstance(metadata_value, dict) else {}
    final_url = metadata.get("sourceURL") or metadata.get("url") or requested_url
    title = metadata.get("title")
    content_type = metadata.get("contentType")
    return ExtractionResult(
        requested_url=requested_url,
        final_url=final_url if isinstance(final_url, str) else requested_url,
        provider="firecrawl",
        content=content,
        title=title if isinstance(title, str) else None,
        content_type=content_type if isinstance(content_type, str) else None,
    )


def _crawl4ai_markdown(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key in ("raw_markdown", "fit_markdown", "markdown_with_citations"):
            candidate = value.get(key)
            if isinstance(candidate, str) and candidate.strip():
                return candidate
    return ""


def parse_crawl4ai_response(requested_url: str, data: Any) -> ExtractionResult:
    if not isinstance(data, dict):
        raise ExtractionError("invalid crawl4ai response")
    results = data.get("results")
    if not isinstance(results, list) or not results or not isinstance(results[0], dict):
        raise ExtractionError("crawl4ai response missing result")
    item = results[0]
    if item.get("success") is False:
        raise ExtractionError(str(item.get("error_message") or "crawl4ai reported failure"))
    content = _usable_content(_crawl4ai_markdown(item.get("markdown")), "crawl4ai")
    metadata_value = item.get("metadata")
    metadata: dict[str, Any] = metadata_value if isinstance(metadata_value, dict) else {}
    final_url = item.get("redirected_url") or item.get("url") or requested_url
    title = metadata.get("title")
    content_type = metadata.get("content_type") or metadata.get("contentType")
    return ExtractionResult(
        requested_url=requested_url,
        final_url=final_url if isinstance(final_url, str) else requested_url,
        provider="crawl4ai",
        content=content,
        title=title if isinstance(title, str) else None,
        content_type=content_type if isinstance(content_type, str) else None,
    )


def make_fetchers(
    settings: Mapping[str, str],
    *,
    timeout: float,
    min_chars: int,
) -> dict[str, Callable[[str], ExtractionResult]]:
    firecrawl_base = (
        settings.get("FIRECRAWL_API_URL")
        or settings.get("FIRECRAWL_BASE_URL")
        or DEFAULT_FIRECRAWL_URL
    ).rstrip("/")
    firecrawl_key = settings.get("FIRECRAWL_API_KEY", "fc-selfhost")
    crawl4ai_base = settings.get("CRAWL4AI_API_URL", "").rstrip("/")
    crawl4ai_token = settings.get("CRAWL4AI_API_TOKEN", "")

    def ensure_minimum(result: ExtractionResult) -> ExtractionResult:
        if len(result.content) < min_chars:
            raise ExtractionError(
                f"{result.provider} returned only {len(result.content)} characters; minimum is {min_chars}"
            )
        return result

    def firecrawl(url: str) -> ExtractionResult:
        validate_public_url(url)
        data = _post_json(
            f"{firecrawl_base}/v1/scrape",
            {"url": url, "formats": ["markdown", "rawHtml"]},
            headers={"Authorization": f"Bearer {firecrawl_key}"},
            timeout=timeout,
        )
        return ensure_minimum(parse_firecrawl_response(url, data))

    def crawl4ai(url: str) -> ExtractionResult:
        validate_public_url(url)
        if not crawl4ai_base:
            raise ExtractionError("CRAWL4AI_API_URL is not configured")
        if not crawl4ai_token:
            raise ExtractionError("CRAWL4AI_API_TOKEN is not configured")
        data = _post_json(
            f"{crawl4ai_base}/crawl",
            {"urls": [url]},
            headers={"Authorization": f"Bearer {crawl4ai_token}"},
            timeout=timeout,
        )
        return ensure_minimum(parse_crawl4ai_response(url, data))

    return {"firecrawl": firecrawl, "crawl4ai": crawl4ai}


def extract_with_fallback(
    url: str,
    *,
    provider: str = "auto",
    max_chars: int = DEFAULT_MAX_CHARS,
    fetchers: Mapping[str, Callable[[str], ExtractionResult]],
) -> ExtractionResult:
    order = ["firecrawl", "crawl4ai"] if provider == "auto" else [provider]
    warnings: list[str] = []
    attempted: list[str] = []
    for name in order:
        attempted.append(name)
        fetcher = fetchers.get(name)
        if fetcher is None:
            warnings.append(f"{name}: provider is unavailable")
            continue
        try:
            result = fetcher(url)
        except ExtractionError as exc:
            warnings.append(f"{name}: {exc}")
            continue
        result.attempted = attempted.copy()
        result.warnings = warnings.copy()
        if len(result.content) > max_chars:
            result.content = result.content[:max_chars]
            result.truncated = True
        return result
    raise ExtractionError("; ".join(warnings) or "no extraction provider available")


def render_json(result: ExtractionResult) -> str:
    return json.dumps(asdict(result), ensure_ascii=False, indent=2)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract a public URL using local Firecrawl with Crawl4AI fallback."
    )
    parser.add_argument("url")
    parser.add_argument(
        "--provider", choices=("auto", "firecrawl", "crawl4ai"), default="auto"
    )
    parser.add_argument("--json", action="store_true", help="emit structured JSON")
    parser.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS)
    parser.add_argument("--min-chars", type=int, default=DEFAULT_MIN_CHARS)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.max_chars < 1 or args.min_chars < 1 or args.timeout <= 0:
        parser.error("--max-chars, --min-chars, and --timeout must be positive")
    try:
        validate_public_url(args.url)
        settings = load_settings(args.config.expanduser())
        result = extract_with_fallback(
            args.url,
            provider=args.provider,
            max_chars=args.max_chars,
            fetchers=make_fetchers(settings, timeout=args.timeout, min_chars=args.min_chars),
        )
    except (ExtractionError, ValueError) as exc:
        print(json.dumps({"error": str(exc), "url": args.url}), file=sys.stderr)
        return 1
    if args.json:
        print(render_json(result))
    else:
        print(result.content)
        print(
            f"[local-web-extract provider={result.provider} attempted={','.join(result.attempted)}]",
            file=sys.stderr,
        )
        for warning in result.warnings:
            print(f"warning: {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
