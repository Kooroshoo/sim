# Chapter N — <Short, evocative title>

> Status: 🔴 not started _(switch to 🟡 in progress, then 🟢 done — keep only one)_

## Concept

Explain the idea as if teaching someone else. If you can't explain it plainly here, you don't understand it
yet — come back and rewrite this section after finishing the project below, not before.

## Why it matters

One or two sentences tying this back to the essentials checklist in the root README, or to a specific target
job posting. Be concrete — "this is in Alignerr's required-skills list" beats "this is generally useful."

## Project

What you're building, concretely. A sentence or two — just enough to know what "done" looks like. Not a full
spec.

## Code walkthrough

Keep snippets short — just the lines that illustrate the concept. Full, compiling code lives in
`0N-chapter-folder/src/`. Embed it directly (single-level include, resolved relative to this file in `pages/`):

```
{{#include ../0N-chapter-folder/src/example.ext:1:10}}
```

(See the root README's "Mixing prose and code" section for the full convention — and why it must be a
single-level include, not nested through another README.)

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

Plots, GIFs, screenshots, or a link to a short demo recording.

## Resources

- <link>

---

**This file is the canonical source** — it belongs in `pages/chapter-N.md`, not in the project folder. Leave a
short pointer file in `0N-chapter-folder/README.md` instead:

```markdown
# Chapter N — <Title>

> Status: 🔴 not started

This chapter is written in [`pages/chapter-N.md`](../pages/chapter-N.md) — read it there, or on the live book.
This folder holds the actual project (`src/` — real, compiling code).
```
