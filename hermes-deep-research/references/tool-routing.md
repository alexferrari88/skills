# Tool Routing

Use this file to decide which Hermes tools to use at each stage.

## `web_search`
Use when:
- mapping the space
- generating subtopic coverage
- finding official docs, news, benchmarks, alternatives, and critics
- finding sources for multiple subquestions quickly

## `web_extract`
Use when:
- a promising source needs full-text reading
- details beyond snippets matter
- reading reports, docs, or articles in full
- you want clean markdown for synthesis

## Browser tools
Use when:
- `web_extract` fails or returns partial content
- the page is JS-rendered
- important content is hidden behind interaction
- visual layout or state matters
- console inspection may reveal errors or failed loads

Preferred sequence:
1. `browser_navigate`
2. `browser_snapshot` or `browser_console(expression=...)`
3. `browser_click` / `browser_scroll` / `browser_type` as needed
4. `browser_vision` only when visual understanding materially helps

## `delegate_task`
Use when:
- the topic has 3+ separable dimensions
- a fast parallel pass will materially improve coverage
- you want an explicit skeptic/counterargument stream
- the user asks for very deep or forensic work

Recommended specialist patterns:
- thesis / anti-thesis / evidence-validation
- architecture / market / risks
- timeline / metrics / criticism

The parent session synthesizes; subagents gather and compress.

## `execute_code`
Use when:
- ranking options
- computing weighted scores
- comparing benchmarks or price tables
- aggregating dates, counts, or timelines
- any arithmetic appears

Never do mental math in prose.

## File tools
Use when:
- the report is long enough to warrant a saved artifact
- the user wants a memo/report file
- reproducibility matters for later follow-up

## `session_search`
Use when:
- the user references prior work
- the topic likely relates to earlier sessions
- follow-up research should build on prior findings

## Escalation Logic

```text
Search weak?       -> broaden queries / search critics / search official docs directly
Extract partial?   -> browser tools
Topic broad?       -> delegate_task
Need scoring?      -> execute_code
Need artifact?     -> write file
Prior context?     -> session_search
```
