"""Provider-aware DSPy loader for Hermes runtime credentials.

This template is meant to be portable across Hermes installations:
- it reads whatever provider/model/base_url Hermes currently resolves to
- it lets callers override `requested_provider` and/or `model`
- it only contains provider-specific logic where the runtime contract forced it

In other words: the helper is generic by default, with a narrow compatibility
branch for Codex-style Responses runtimes.
"""

from __future__ import annotations

import base64
import json
from typing import Any

import dspy
from dspy.clients.base_lm import BaseLM
from hermes_cli.config import load_config
from hermes_cli.runtime_provider import resolve_runtime_provider
from agent.auxiliary_client import resolve_provider_client


class HermesCodexDSPyLM(BaseLM):
    """DSPy BaseLM wrapper for Hermes Codex runtime.

    Why this exists:
    DSPy's built-in `dspy.LM(..., model_type="responses")` routes through
    LiteLLM's Responses API path. Hermes's current ChatGPT Codex endpoint
    requires a slightly different contract (`instructions`, `store=False`,
    streaming semantics), which Hermes already handles via
    `CodexAuxiliaryClient` in `agent.auxiliary_client`.

    So for Codex-backed Hermes runtimes we bypass bare `dspy.LM` and expose a
    chat-completions-shaped client to DSPy instead.
    """

    def __init__(
        self,
        *,
        model: str,
        client: Any,
        temperature: float = 0.0,
        max_tokens: int = 1000,
        cache: bool = True,
        **kwargs: Any,
    ):
        super().__init__(
            model=model,
            model_type="chat",
            temperature=temperature,
            max_tokens=max_tokens,
            cache=cache,
            **kwargs,
        )
        self._client = client

    def forward(
        self,
        prompt: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ):
        messages = messages or [{"role": "user", "content": prompt or ""}]
        merged = {**self.kwargs, **kwargs}

        response = self._client.chat.completions.create(
            model=self.model,
            messages=messages,
            **merged,
        )

        usage = getattr(response, "usage", None)
        if usage is not None and not isinstance(usage, dict):
            response.usage = {
                "prompt_tokens": int(getattr(usage, "prompt_tokens", 0) or 0),
                "completion_tokens": int(getattr(usage, "completion_tokens", 0) or 0),
                "total_tokens": int(getattr(usage, "total_tokens", 0) or 0),
            }
        elif usage is None:
            response.usage = {
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
            }

        if not hasattr(response, "model"):
            response.model = self.model
        return response


def _config_default_model() -> str:
    config = load_config()
    model_cfg = config.get("model") if isinstance(config, dict) else {}
    if not isinstance(model_cfg, dict):
        return ""
    return str(model_cfg.get("default") or model_cfg.get("model") or "").strip()


def _extract_chatgpt_account_id(token: str) -> str | None:
    parts = (token or "").split(".")
    if len(parts) < 2:
        return None
    try:
        payload = parts[1] + "=" * (-len(parts[1]) % 4)
        decoded = base64.urlsafe_b64decode(payload)
        claims = json.loads(decoded)
    except Exception:
        return None

    auth_claim = claims.get("https://api.openai.com/auth")
    if not isinstance(auth_claim, dict):
        return None

    account_id = auth_claim.get("chatgpt_account_id") or auth_claim.get("account_id")
    if isinstance(account_id, str) and account_id.strip():
        return account_id.strip()
    return None


def _normalize_dspy_model_name(provider: str, api_mode: str, model: str) -> str:
    model = (model or "").strip()
    if not model:
        raise ValueError("Model name is empty. Pass model=... or set model.default in Hermes config.")
    if "/" in model:
        return model
    if provider == "anthropic" or api_mode == "anthropic_messages":
        return f"anthropic/{model}"
    return f"openai/{model}"


def load_hermes_dspy_lm(
    model: str | None = None,
    *,
    requested_provider: str | None = None,
    originator: str = "hermes-dspy-runtime",
    use_developer_role: bool = True,
    **lm_overrides: Any,
):
    """Build a DSPy-compatible LM from Hermes runtime state.

    Portability goals:
    - Reuse Hermes runtime resolution instead of hardcoding env vars.
    - Track provider/model changes automatically for most providers.
    - Allow callers to override provider/model while still using Hermes auth.
    - Keep provider-specific adaptation narrow and explicit.

    Current special case:
    - Codex-backed Responses runtimes use a custom BaseLM wrapper around
      Hermes's Codex auxiliary shim, because that live endpoint needed extra
      compatibility handling.

    This function does not make a network call by itself; it only constructs
    the LM object.
    """

    runtime = resolve_runtime_provider(requested=requested_provider)
    provider = str(runtime.get("provider") or "").strip().lower()
    api_mode = str(runtime.get("api_mode") or "chat_completions").strip().lower()
    base_url = str(runtime.get("base_url") or "").strip().rstrip("/")
    api_key = str(runtime.get("api_key") or "").strip()

    if not api_key:
        raise ValueError("Hermes runtime resolved without an API key/token.")
    if not base_url:
        raise ValueError("Hermes runtime resolved without a base URL.")

    model_name = _normalize_dspy_model_name(provider, api_mode, model or _config_default_model())

    headers: dict[str, str] = {"User-Agent": f"DSPy/{dspy.__version__}"}
    if provider == "openai-codex" or api_mode == "codex_responses":
        headers["OpenAI-Beta"] = "responses=experimental"
        headers["originator"] = originator
        account_id = _extract_chatgpt_account_id(api_key)
        if account_id:
            headers["chatgpt-account-id"] = account_id

        wire_model = model_name.split('/', 1)[1] if '/' in model_name else model_name
        client, resolved_model = resolve_provider_client(
            "custom",
            model=wire_model,
            explicit_base_url=base_url,
            explicit_api_key=api_key,
            api_mode="codex_responses",
        )
        if client is None:
            raise ValueError("Failed to build Hermes Codex auxiliary client.")

        return HermesCodexDSPyLM(
            model=resolved_model or wire_model,
            client=client,
            headers=headers,
            cache=bool(lm_overrides.pop("cache", True)),
            use_developer_role=use_developer_role,
            **lm_overrides,
        )

    kwargs: dict[str, Any] = {
        "api_base": base_url,
        "api_key": api_key,
        "use_developer_role": use_developer_role,
        **lm_overrides,
    }

    if headers:
        kwargs["headers"] = {**headers, **dict(kwargs.get("headers") or {})}

    model_type = "chat"
    return dspy.LM(model_name, model_type=model_type, **kwargs)


def load_hermes_rlm(signature: str, *, model: str | None = None, **rlm_kwargs: Any) -> dspy.RLM:
    """Convenience wrapper: build the Hermes-authenticated LM and pass it as sub_lm."""
    lm = load_hermes_dspy_lm(model=model)
    return dspy.RLM(signature, sub_lm=lm, **rlm_kwargs)


if __name__ == "__main__":
    lm = load_hermes_dspy_lm()
    print(
        {
            "lm_class": type(lm).__name__,
            "model": lm.model,
            "model_type": getattr(lm, "model_type", None),
            "header_keys": sorted((getattr(lm, "kwargs", {}).get("headers") or {}).keys()),
        }
    )
