# <Short, evocative title>

> Status: 🔴 not started _(switch to 🟡 in progress, then 🟢 done — keep only one)_

## Concept

Explain the idea as if teaching someone else. If you can't explain it plainly here, you don't understand it
yet — come back and rewrite this section after finishing the project below, not before.

## Why it matters

One or two sentences tying this back to a specific target job posting. Be concrete — "this is in Alignerr's
required-skills list" beats "this is generally useful."

## Must-knows for interviews

The specific things interviewers actually probe for this topic — not a generic list of subtopics. Each bullet
should be something you could be asked a follow-up question about and have a real answer for.

## Project

What you're building, concretely. A sentence or two — just enough to know what "done" looks like. Not a full
spec.

## Code walkthrough

Keep snippets short — just the lines that illustrate the concept. Full, compiling code lives in
`<parent>/src/` (e.g. `ros/src/`, `rl/src/`). Embed it directly — **single-level include**, resolved relative
to this file's location at `pages/<parent>/0N-name.md` (note the `../../` — two levels up to the repo root,
then down into the project folder) — and **the fence must have a language tag** (` ```cpp `, ` ```python `,
etc.) or there's no syntax highlighting:

```cpp
{{#include ../../<parent>/src/example.ext:1:10}}
```

For a concept that applies equally to C++ and Python (most ROS2 examples), use the tab component instead of a
single fence — see the root README's "Mixing prose and code" section for the exact markup, and why blank lines
around each fence are required.

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

**This file is the canonical source** — it belongs in `pages/<parent>/0N-name.md`, not in the project folder.
The project folder's `README.md` (one per parent section, not per subsection) is just a short pointer:

```markdown
# <Parent Section Name>

> Status: 🔴 not started

This section is written across [`pages/<parent>/*.md`](../pages/<parent>/) — read it there, or on the live
book. This folder holds the actual project (`src/` — real, compiling code).
```
