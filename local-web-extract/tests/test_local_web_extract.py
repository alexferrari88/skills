from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "local_web_extract.py"
spec = importlib.util.spec_from_file_location("local_web_extract", MODULE_PATH)
assert spec is not None and spec.loader is not None
local_web_extract = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = local_web_extract
spec.loader.exec_module(local_web_extract)


class UrlValidationTests(unittest.TestCase):
    def test_rejects_private_ip_literal(self) -> None:
        with self.assertRaisesRegex(ValueError, "private or reserved"):
            local_web_extract.validate_public_url("http://127.0.0.1/admin")

    def test_rejects_non_http_scheme(self) -> None:
        with self.assertRaisesRegex(ValueError, "http or https"):
            local_web_extract.validate_public_url("file:///etc/passwd")


class ResponseParsingTests(unittest.TestCase):
    def test_parses_nested_firecrawl_response(self) -> None:
        result = local_web_extract.parse_firecrawl_response(
            "https://example.com",
            {
                "success": True,
                "data": {
                    "markdown": "# Example\n\nUseful body",
                    "metadata": {
                        "title": "Example",
                        "sourceURL": "https://example.com/final",
                        "contentType": "text/html",
                    },
                },
            },
        )

        self.assertEqual(result.provider, "firecrawl")
        self.assertEqual(result.final_url, "https://example.com/final")
        self.assertEqual(result.title, "Example")
        self.assertEqual(result.content, "# Example\n\nUseful body")

    def test_parses_crawl4ai_markdown_object(self) -> None:
        result = local_web_extract.parse_crawl4ai_response(
            "https://example.com",
            {
                "success": True,
                "results": [
                    {
                        "success": True,
                        "url": "https://example.com/final",
                        "markdown": {"raw_markdown": "# Example\n\nCrawl4AI body"},
                        "metadata": {"title": "Example"},
                    }
                ],
            },
        )

        self.assertEqual(result.provider, "crawl4ai")
        self.assertEqual(result.final_url, "https://example.com/final")
        self.assertEqual(result.content, "# Example\n\nCrawl4AI body")


class FallbackTests(unittest.TestCase):
    def test_auto_falls_back_to_crawl4ai_and_reports_firecrawl_error(self) -> None:
        calls: list[str] = []

        def firecrawl(_url: str):
            calls.append("firecrawl")
            raise local_web_extract.ExtractionError("empty markdown")

        def crawl4ai(url: str):
            calls.append("crawl4ai")
            return local_web_extract.ExtractionResult(
                requested_url=url,
                final_url=url,
                provider="crawl4ai",
                content="# Success\n\nFallback content",
            )

        result = local_web_extract.extract_with_fallback(
            "https://example.com",
            provider="auto",
            fetchers={"firecrawl": firecrawl, "crawl4ai": crawl4ai},
        )

        self.assertEqual(calls, ["firecrawl", "crawl4ai"])
        self.assertEqual(result.provider, "crawl4ai")
        self.assertEqual(result.attempted, ["firecrawl", "crawl4ai"])
        self.assertEqual(result.warnings, ["firecrawl: empty markdown"])

    def test_forced_provider_does_not_fall_back(self) -> None:
        calls: list[str] = []

        def firecrawl(_url: str):
            calls.append("firecrawl")
            raise local_web_extract.ExtractionError("failed")

        def crawl4ai(_url: str):
            calls.append("crawl4ai")
            raise AssertionError("must not be called")

        with self.assertRaisesRegex(local_web_extract.ExtractionError, "firecrawl: failed"):
            local_web_extract.extract_with_fallback(
                "https://example.com",
                provider="firecrawl",
                fetchers={"firecrawl": firecrawl, "crawl4ai": crawl4ai},
            )

        self.assertEqual(calls, ["firecrawl"])

    def test_truncates_content_and_marks_result(self) -> None:
        def firecrawl(url: str):
            return local_web_extract.ExtractionResult(
                requested_url=url,
                final_url=url,
                provider="firecrawl",
                content="abcdefghij",
            )

        result = local_web_extract.extract_with_fallback(
            "https://example.com",
            provider="auto",
            max_chars=5,
            fetchers={"firecrawl": firecrawl},
        )

        self.assertEqual(result.content, "abcde")
        self.assertTrue(result.truncated)


class EnvFileTests(unittest.TestCase):
    def test_reads_shell_and_colon_style_values_without_executing_file(self) -> None:
        values = local_web_extract.parse_env_text(
            "XAI_API_KEY: ignored\nCRAWL4AI_API_TOKEN=secret-token\nexport OTHER='value'\n"
        )

        self.assertEqual(values["CRAWL4AI_API_TOKEN"], "secret-token")
        self.assertEqual(values["OTHER"], "value")


class SerializationTests(unittest.TestCase):
    def test_json_output_contains_provider_attempts_and_content(self) -> None:
        result = local_web_extract.ExtractionResult(
            requested_url="https://example.com",
            final_url="https://example.com/",
            provider="firecrawl",
            content="# Example",
            attempted=["firecrawl"],
        )

        payload = json.loads(local_web_extract.render_json(result))

        self.assertEqual(payload["provider"], "firecrawl")
        self.assertEqual(payload["attempted"], ["firecrawl"])
        self.assertEqual(payload["content"], "# Example")


if __name__ == "__main__":
    unittest.main()
