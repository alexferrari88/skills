"""Experimental RLM helper that exposes Hermes web_search inside dspy.RLM.

This is intentionally additive and reversible:
- it does NOT replace the existing stable templates
- it reuses the stable Hermes runtime-auth loader
- it adds one experimental bridge tool: web_search

If this experiment turns out not to be worth keeping, simply stop using this
file and fall back to `templates/hermes_dspy_runtime.py`.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from typing import Any, Callable

import dspy
from dspy.primitives.python_interpreter import PythonInterpreter
from model_tools import handle_function_call


def _load_base_runtime_module():
    path = Path(__file__).with_name("hermes_dspy_runtime.py")
    spec = importlib.util.spec_from_file_location("hermes_dspy_runtime", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Failed to load base runtime template: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_BASE = _load_base_runtime_module()
load_hermes_dspy_lm = _BASE.load_hermes_dspy_lm


def make_hermes_web_search_tool(
    *,
    call_log: list[dict[str, Any]] | None = None,
    max_results: int = 5,
) -> Callable[[str], dict[str, Any]]:
    """Create a compact Hermes-backed web_search tool for dspy.RLM.

    The return payload is intentionally small so the REPL environment does not
    get flooded with unnecessary text.
    """

    capped_results = max(1, int(max_results))

    def web_search(query: str) -> dict[str, Any]:
        """Search the web via Hermes and return a compact top-results list."""
        try:
            raw = handle_function_call("web_search", {"query": query})
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {"error": raw}

            items = ((payload.get("data") or {}).get("web") or [])[:capped_results]
            compact = [
                {
                    "title": str(item.get("title") or ""),
                    "url": str(item.get("url") or ""),
                    "description": str(item.get("description") or ""),
                }
                for item in items
            ]
            result = {
                "query": query,
                "results": compact,
                "count": len(compact),
            }
        except Exception as exc:
            result = {
                "query": query,
                "results": [],
                "count": 0,
                "error": f"{type(exc).__name__}: {exc}",
            }

        if call_log is not None:
            call_log.append(result)
        return result

    return web_search


def make_python_interpreter_with_auto_node_modules() -> PythonInterpreter:
    """Create a PythonInterpreter that asks Deno to auto-manage node modules.

    This stays in the experimental layer so we do not alter stable templates or
    Hermes core just to test tool-bridged RLM behavior.
    """
    interp = PythonInterpreter()
    if "--node-modules-dir=auto" not in interp.deno_command:
        try:
            run_index = interp.deno_command.index("run")
            interp.deno_command.insert(run_index + 1, "--node-modules-dir=auto")
        except ValueError:
            interp.deno_command.insert(1, "--node-modules-dir=auto")
    return interp


def load_hermes_rlm_with_web_search(
    signature: str,
    *,
    model: str | None = None,
    requested_provider: str | None = None,
    web_search_max_results: int = 5,
    call_log: list[dict[str, Any]] | None = None,
    tools: list[Callable] | None = None,
    interpreter: PythonInterpreter | None = None,
    **rlm_kwargs: Any,
) -> tuple[dspy.RLM, list[dict[str, Any]]]:
    """Build a Hermes-authenticated RLM and expose a Hermes web_search tool.

    Returns:
        (rlm, call_log)
    """
    lm = load_hermes_dspy_lm(model=model, requested_provider=requested_provider)
    tool_log = call_log if call_log is not None else []
    merged_tools = list(tools or [])
    merged_tools.append(
        make_hermes_web_search_tool(
            call_log=tool_log,
            max_results=web_search_max_results,
        )
    )
    rlm_kwargs = dict(rlm_kwargs)
    rlm_kwargs.setdefault("interpreter", interpreter or make_python_interpreter_with_auto_node_modules())
    rlm = dspy.RLM(signature, sub_lm=lm, tools=merged_tools, **rlm_kwargs)
    return rlm, tool_log


if __name__ == "__main__":
    rlm, log = load_hermes_rlm_with_web_search(
        "context, query -> answer",
        max_iterations=1,
        max_llm_calls=1,
    )
    print(
        {
            "rlm_type": type(rlm).__name__,
            "tool_names": sorted(rlm._user_tools.keys()),
            "log_entries": len(log),
        }
    )
