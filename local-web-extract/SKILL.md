---
name: local-web-extract
description: Extract full content from webpages, articles, PDFs, and JavaScript-heavy URLs through self-hosted Firecrawl with automatic Crawl4AI fallback. Use when ordinary built-in web fetching fails, is incomplete, or when the user asks for full page extraction. Do not use metered Parallel extraction unless explicitly requested.
version: 1.0.0
author: Alex Ferrari
license: MIT
compatibility: Requires Python 3 and access to configured self-hosted Firecrawl/Crawl4AI services.
---

# Local Web Extraction

Use the client's ordinary web search or fetch first when it is sufficient. Use this skill when:

- ordinary fetching fails, is blocked, or returns empty/incomplete content
- JavaScript rendering is required
- the user requests the full content of a URL
- a difficult webpage or PDF needs a self-hosted extraction fallback

For Firecrawl search, site mapping, multi-URL structured extraction, raw API access, health checks, or service troubleshooting, use the `firecrawl` skill instead.

## Default command

```bash
local-web-extract --json "https://example.com"
```

The command validates the target and automatically tries:

1. self-hosted Firecrawl
2. self-hosted Crawl4AI if Firecrawl fails or returns inadequate Markdown

Parse the returned JSON. Use `content` as the extracted body, and preserve `final_url`, `title`, `provider`, `attempted`, `warnings`, and `truncated` when they matter to the answer.

## Diagnostics

Force one provider only when troubleshooting or comparing extraction:

```bash
local-web-extract --provider firecrawl --json "https://example.com"
local-web-extract --provider crawl4ai --json "https://example.com"
```

Useful limits:

```bash
local-web-extract --max-chars 100000 --timeout 90 --json "https://example.com"
```

## Failure handling

- A non-zero exit means no requested provider returned usable content.
- Surface the reported provider errors; never invent or reconstruct missing page content.
- If `provider` is `crawl4ai`, mention a Firecrawl warning only when it materially affects the task or indicates degraded infrastructure.
- If both local providers fail and browser automation is available, use the browser as the next fallback.
- Do not run `parallel-cli extract` unless the user explicitly requests Parallel's extraction service.

## Configuration

The helper reads `~/.config/local-web-extract/config.env`, then allows process environment variables to override it:

```text
FIRECRAWL_API_URL=http://127.0.0.1:8081
# Legacy alias used only when FIRECRAWL_API_URL is unset:
FIRECRAWL_BASE_URL=http://127.0.0.1:8081
FIRECRAWL_API_KEY=fc-selfhost
CRAWL4AI_API_URL=https://crawler.example.internal
CRAWL4AI_ENV_FILE=/path/to/crawl4ai.env
```

`CRAWL4AI_ENV_FILE` is parsed as data rather than sourced as shell code. It should contain `CRAWL4AI_API_TOKEN`. A directly exported `CRAWL4AI_API_TOKEN` takes precedence.
