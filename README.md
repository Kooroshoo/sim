# sim — Simulation, ROS2 & Robot Learning

Hands-on practice repo for the **simulation/digital-twin engineer** niche (not generalist robotics): 3D
simulation engines + robotics middleware + RL + VR/AR teleoperation. Scope is deliberately narrow — see
"Why this scope" below — and maps directly to what NVIDIA, Oversonic, Xaba, Qualcomm, Accenture Physical AI,
and the Alignerr/Mindrift/Micro1/Toptal remote roles actually ask for.

> Last updated: **17 Nov 2026**

**This is both a book and a project.** Each subsection below is a concept write-up *and* the working
code/experiments for that concept — read it top to bottom like a book, or jump straight to the code.

📖 **Live book:** https://kooroshoo.github.io/sim/ (built with [mdBook](https://rust-lang.github.io/mdBook/),
auto-deployed on every push to `main` — see `.github/workflows/deploy-book.yml`)

---

## 📖 Table of contents

| Section | Subsections | Status |
|---|---|---|
| [**ROS**](./ros/) — working fluency, ~30% | [Fundamentals](./pages/ros/01-fundamentals.md) · [Gazebo](./pages/ros/02-gazebo.md) · [RViz](./pages/ros/03-rviz.md) · [Nav2](./pages/ros/04-nav2.md) · [MoveIt](./pages/ros/05-moveit.md) | 🔴 not started |
| [**RL**](./rl/) — primary depth, ~70% | [Fundamentals](./pages/rl/01-fundamentals.md) · [MuJoCo](./pages/rl/02-mujoco.md) · [Isaac Lab](./pages/rl/03-isaac-lab.md) · [Sim-to-Real](./pages/rl/04-sim-to-real.md) · [Imitation Learning & VLA](./pages/rl/05-imitation-learning-vla.md) · [Flagship Project](./pages/rl/06-flagship-project.md) | 🔴 not started |
| [**System Design**](./system-design/) — interview-ready, built on ROS+RL experience | [Parallel Sim Pipeline](./pages/system-design/01-parallel-sim-pipeline.md) · [SDG Pipeline](./pages/system-design/02-sdg-pipeline.md) · [Digital Twin Sync](./pages/system-design/03-digital-twin-sync.md) · [Sim-to-Real Validation](./pages/system-design/04-sim-to-real-validation.md) · [VR/AR Teleop](./pages/system-design/05-vr-ar-teleop.md) · [Sensor Fusion](./pages/system-design/06-sensor-fusion.md) · [Real-Time Control](./pages/system-design/07-real-time-control.md) · [Fault-Tolerant Nav](./pages/system-design/08-fault-tolerant-nav.md) | 🔴 not started |
| [Appendices](./notes/) | Short standalone essays: QoS cheatsheet, PPO vs SAC, Kalman derivation | ongoing |

---

## Why this scope

Robotics is too broad a target on its own — SLAM, manipulation, legged locomotion, swarm robotics, aerial
robotics are each their own specialization. This repo stays anchored to the intersection that's actually the
differentiator: **simulation fidelity + sim-to-real/RL + middleware integration + VR/AR**, mirroring the
resume categories (Simulation Engines | Robotics Middleware | Computer Vision & RL | VR/AR) and what target
job postings weight — simulation/RL as primary depth, ROS2 as working fluency to wire things together
(~70/30), not the reverse.

**System Design comes last on purpose** (not first): these prompts are far more concrete once you've built
even a small version of one of these systems in ROS/RL — practiced cold, they become buzzword-matching
instead of reasoning you can defend under a follow-up question.

---

## Subsection template

Every subsection page (`pages/ros/0N-*.md`, `pages/rl/0N-*.md`) follows the same shape, so it reads
consistently as both a book and a project log. Copy [`_template/`](./_template/) to start a new one — it's the
single canonical template, don't duplicate the shape by hand:

```
## Concept
What this subsection covers, explained as if teaching someone else (Feynman-style — if you can't explain it
plainly, you don't know it yet).

## Why it matters
Tie back to target job postings — why this concept, not just that it exists.

## Must-knows for interviews
The specific things interviewers actually probe — not a generic topic list.

## Project
What you're building to prove the concept, concretely.

## Log
Dated entries: what you tried, what failed first, what you changed.

## Results
Code links, plots, GIFs, demo recordings.

## Resources
Links used while writing this subsection.
```

System Design subsections use a lighter variant (`Prompt` + `Things to cover when narrating` instead of
`Concept`/`Project`, since the deliverable is a sketch + spoken narration, not running code) — see any file in
`pages/system-design/` for the pattern.

---

## Mixing prose and code

**Write code in real, runnable files; show only short excerpts in the page; never paste a full copy of the
code into markdown.** Two reasons: copy-pasted code drifts out of sync with what actually compiles the moment
either one changes, and it clutters the "book" read with boilerplate (includes, imports, setup) nobody needs
to read twice.

**Important: the content lives in `pages/<section>/0N-name.md`, not in the project folder's `README.md`.**
Each project folder's `README.md` is just a short pointer to the real pages. This isn't arbitrary — it's a fix
for a real mdBook bug: `{{#include}}` directives nested two levels deep (a page including a project `README.md`,
which itself includes a code file) resolve their paths incorrectly. A single-level include — the page
embedding code directly — resolves correctly every time. Don't fight this by nesting includes again later;
keep the page content and its code includes in the same file.

Convention:
1. Real code lives in each project folder's `src/` (e.g. `ros/src/controller.cpp`) — compilable, runnable,
   the actual project.
2. The page embeds the relevant lines with mdBook's `{{#include}}` directive, by line range, relative to its
   own location (note the extra `../` level since pages now live one folder deeper, e.g. `pages/ros/...`):

   ```
   {{#include ../../ros/src/controller.cpp:10:20}}
   ```

   This always shows the *current* file contents — there is nothing to keep in sync by hand.
3. **The code fence needs a language tag** (` ```cpp `, ` ```python `) — a bare ` ``` ` disables syntax
   highlighting entirely, a bug hit once already in this repo.
4. Don't hyperlink to sibling folders (e.g. `[src/](./src/)`) from inside page prose — refer to `src/` as
   plain inline code instead; the file tree is one click away on GitHub, and the book shows the code directly
   via `{{#include}}` anyway.

**C++/Python tabs**: when a concept applies equally to both (most ROS2 examples, since `rclcpp`/`rclpy` are
both first-class), show both via the tab component (CSS in `custom.css`, JS in `custom.js`):

```html
<div class="code-tabs">
<div class="code-tabs-nav">
<button class="code-tab-btn active" onclick="simShowTab(this, 'cpp')">C++</button>
<button class="code-tab-btn" onclick="simShowTab(this, 'python')">Python</button>
</div>
<div class="code-tab-panel active" data-lang="cpp">

```cpp
{{#include ../../ros/src/example.cpp:1:10}}
```

</div>
<div class="code-tab-panel" data-lang="python">

```python
{{#include ../../ros/src/example.py:1:10}}
```

</div>
</div>
```

The blank lines around each fenced code block are required — without them mdBook's markdown parser treats the
whole `<div>...</div>` as one raw HTML block and never renders the code fence as markdown at all.

For **ROS2 C++ code**, scaffold with `ros2 pkg create --build-type ament_cmake <name>` rather than hand-
rolling a `CMakeLists.txt` — it generates the right boilerplate for you. For **Python/RL code**, just `.py`
files in `src/`, optionally a `requirements.txt`.

---

## Adding a new subsection

1. Pick the parent (`ros/`, `rl/`, or `system-design/`) and the next `0N-` number
2. Write the real code in `<parent>/src/` (or `<parent>/assets/` for system-design sketches)
3. Copy [`_template/`](./_template/)'s content into `pages/<parent>/0N-name.md` — that's the canonical source
4. Embed code excerpts via a single-level `{{#include ../../<parent>/src/file.ext:L:L}}`, fenced with a
   language tag
5. Add it to `pages/SUMMARY.md`, the parent's `index.md`, and the table of contents above
6. Push to `main` — the GitHub Actions workflow rebuilds and redeploys the book automatically

---

## 📝 Learning log

| Date | Worked on | What I learned / what failed | Next |
|---|---|---|---|
| | | | |
