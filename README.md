# sim — Simulation, ROS2 & Robot Learning

Hands-on practice repo for the **simulation/digital-twin engineer** niche (not generalist robotics): 3D
simulation engines + robotics middleware + RL + VR/AR teleoperation. Scope is deliberately narrow — see
"Why this scope" below — and maps directly to what NVIDIA, Oversonic, Xaba, Qualcomm, Accenture Physical AI,
and the Alignerr/Mindrift/Micro1/Toptal remote roles actually ask for.

> Last updated: **17 Nov 2026**

**This is both a book and a project.** Each numbered chapter below is a concept write-up *and* the working
code/experiments for that concept — read it top to bottom like a book, or jump straight to the code.

📖 **Live book:** https://kooroshoo.github.io/sim/ (built with [mdBook](https://rust-lang.github.io/mdBook/),
auto-deployed on every push to `main` — see `.github/workflows/deploy-book.yml`)

---

## 📖 Table of contents

| # | Chapter | Covers | Status |
|---|---|---|---|
| 1 | [ROS2 + Gazebo — Giving Simulation a Voice](./01-ros-gazebo/) | Nodes, topics/services/actions, QoS, a simulated diff-drive robot | 🔴 not started |
| 2 | [RL Fundamentals — Teaching a Policy to Move](./02-rl-mujoco/) | PPO/SAC on MuJoCo, reward shaping, easy → hard tasks | 🔴 not started |
| 3 | [Scaling Up — Isaac Lab, Domain Randomization & Sim-to-Real](./03-isaac-lab/) | GPU-parallel envs, domain randomization, flagship portfolio project | 🔴 not started |
| — | [Appendices](./notes/) | Short standalone essays: QoS cheatsheet, PPO vs SAC, Kalman derivation, simulation-systems design sketches | ongoing |

---

## Why this scope

Robotics is too broad a target on its own — SLAM, manipulation, legged locomotion, swarm robotics, aerial
robotics are each their own specialization. This repo stays anchored to the intersection that's actually the
differentiator: **simulation fidelity + sim-to-real/RL + middleware integration + VR/AR**, mirroring the
resume categories (Simulation Engines | Robotics Middleware | Computer Vision & RL | VR/AR) and what target
job postings weight — simulation/RL as primary depth, ROS2 as working fluency to wire things together
(~70/30), not the reverse.

---

## Chapter template

Every chapter folder (`01-`, `02-`, `03-...`) follows the same shape, so it reads consistently as both a book
and a project log. Copy [`_template/`](./_template/) to start a new one — it's the single canonical template,
don't duplicate the shape by hand:

```
## Concept
What this chapter covers, explained as if teaching someone else (Feynman-style — if you can't explain it
plainly, you don't know it yet).

## Why it matters
Tie back to the essentials checklist / target job postings — why this concept, not just that it exists.

## Project
What you're building to prove the concept, concretely.

## Log
Dated entries: what you tried, what failed first, what you changed.

## Results
Code links, plots, GIFs, demo recordings.

## Resources
Links used while writing this chapter.
```

---

## Mixing prose and code

**Write code in real, runnable files; show only short excerpts in the chapter; never paste a full copy of the
code into markdown.** Two reasons: copy-pasted code drifts out of sync with what actually compiles the moment
either one changes, and it clutters the "book" read with boilerplate (includes, imports, setup) nobody needs
to read twice.

**Important: the chapter content lives in `pages/chapter-N.md`, not in the project folder's `README.md`.**
Each project folder's `README.md` is just a short pointer to the real chapter. This isn't arbitrary — it's a
fix for a real mdBook bug: `{{#include}}` directives nested two levels deep (a `pages/` stub including a
project `README.md`, which itself includes a code file) resolve their paths incorrectly. A single-level
include — `pages/chapter-N.md` embedding code directly — resolves correctly every time. Don't fight this by
nesting includes again later; keep the chapter content and its code includes in the same file.

Convention:
1. Real code lives in each chapter's `src/` (e.g. `01-ros-gazebo/src/controller.cpp`) — compilable, runnable,
   the actual project.
2. `pages/chapter-N.md` embeds the relevant lines with mdBook's `{{#include}}` directive, by line range,
   relative to its own location in `pages/`:

   ```
   {{#include ../01-ros-gazebo/src/controller.cpp:10:20}}
   ```

   This always shows the *current* file contents — there is nothing to keep in sync by hand. On GitHub's
   plain file view the raw `{{#include ...}}` text shows as-is (harmless, just not rendered); on the deployed
   book (where it matters most, since that's the polished reading experience) it renders as a real, correctly
   highlighted code block.
3. Don't hyperlink to sibling folders (e.g. `[src/](./src/)`) from inside chapter prose — refer to `src/` as
   plain inline code instead; the file tree is one click away on GitHub, and the book shows the code directly
   via `{{#include}}` anyway.

For **ROS2 C++ chapters**, scaffold with `ros2 pkg create --build-type ament_cmake <name>` inside the chapter
folder rather than hand-rolling a `CMakeLists.txt` — it generates the right boilerplate for you. For
**standalone C++** (non-ROS2), a minimal `CMakeLists.txt` + `src/` is enough. For **Python/RL chapters**, just
`.py` files in `src/`, optionally a `requirements.txt`.

---

## Adding a new chapter

1. Create `0N-chapter-name/src/` for the real code, and `0N-chapter-name/README.md` as a short pointer
   (see the template's bottom section for the exact pointer text)
2. Copy [`_template/`](./_template/)'s main content into `pages/chapter-N.md` — that's the canonical source
3. Fill in `Concept` / `Why it matters` / `Project`, write the code in `src/`, embed excerpts via a
   single-level `{{#include ../0N-chapter-name/src/file.ext:L:L}}`
4. Add it to `pages/SUMMARY.md` and the table of contents above
5. Push to `main` — the GitHub Actions workflow rebuilds and redeploys the book automatically

---

## Essentials checklist

### ROS2 (working fluency — not deep specialization)
- [ ] Nodes, topics, services, actions — when to use each
- [ ] QoS profiles — `RELIABLE` vs `BEST_EFFORT`, durability, history depth (control vs telemetry)
- [ ] DDS discovery mechanics (and the ROS1 master → ROS2 DDS story)
- [ ] Lifecycle nodes (unconfigured → inactive → active → finalized)
- [ ] `MultiThreadedExecutor` vs blocking `rclcpp::spin` — and why production systems need the former
- [ ] URDF basics (robot description: links, joints, sensors)
- [ ] `rviz2` for visualization/debugging
- Resource: [ROS2 docs](https://docs.ros.org/en/rolling/)

### Simulation platforms
- [ ] Gazebo (`gz-sim`): worlds, plugins, sensors, the `ros_gz` bridge
- [ ] MuJoCo: MJCF format, physics stepping, contact dynamics, Gymnasium integration
- [ ] Isaac Sim vs Isaac Lab — know the distinction cold (Isaac Sim = high-fidelity SIL/HIL + synthetic
      data; Isaac Lab = lightweight RL/imitation-learning framework built on top)
- [ ] USD basics (Isaac Sim/Omniverse and most digital-twin roles assume this)
- [ ] GPU-accelerated parallel simulation (Isaac Gym lineage) — why it matters for RL throughput
- Resource: [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)

### Reinforcement & imitation learning
- [ ] PPO vs SAC — tradeoffs, when to use which
- [ ] Reward shaping pitfalls (reward hacking, sparse vs dense rewards)
- [ ] Domain randomization — what it's actually solving for
- [ ] Sim-to-real gap — *why* transfer fails, not just that it's hard
- [ ] Imitation learning / behavior cloning basics, and a working sense of Vision-Language-Action (VLA)
      models — this came up repeatedly across target postings (NVIDIA, Amazon, STMicroelectronics) as the
      current direction of the field
- Resource: [OpenAI Spinning Up](https://spinningup.openai.com/) · [Sutton & Barto (free)](http://incompleteideas.net/book/the-book.html)

### Computer vision / synthetic data
- [ ] Synthetic data generation (SDG) workflow — domain randomization for perception, labeling, dataset
      versioning
- [ ] Camera/LiDAR/IMU sensor simulation basics
- [ ] Core CV you already have (OpenCV) applied *to* simulated sensor output, not just real images

### VR/AR + teleoperation
- [ ] OpenXR basics
- [ ] Teleoperation data-collection pipeline concept — latency budget headset/controller → sim or real
      robot, recording/replay for imitation learning (you already have this from Meta Quest/VR work — it's a
      genuine differentiator most candidates won't have an answer for)

### C++ & systems
- [ ] RAII / smart pointers / ownership
- [ ] Concurrency (threads, locks, lock-free basics) — ties directly to the ROS2 executor topic above
- [ ] Real-time constraints, conceptually (latency budgets, why it matters for control loops)

### Simulation-systems design (practice sketching + narrating out loud)
- [ ] Scalable parallel-simulation pipeline (thousands of Isaac Sim/Isaac Gym envs for RL training) — GPU
      utilization, environment resets, throughput vs fidelity tradeoffs
- [ ] Synthetic data generation pipeline for a perception model
- [ ] Digital twin architecture synced with a changing physical asset — sensor ingestion, calibration loop,
      drift detection
- [ ] Sim-to-real validation framework
- [ ] VR/AR teleoperation data-collection pipeline

---

## 📝 Learning log

| Date | Worked on | What I learned / what failed | Next |
|---|---|---|---|
| | | | |
