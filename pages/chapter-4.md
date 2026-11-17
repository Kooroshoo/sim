# Chapter 4 — System Design: Simulation & Robotics Systems

> Status: 🔴 not started

## Concept

Not classical robotics system design (fleet management, autonomy stacks) — **simulation-systems design**,
since that's what your actual target roles probe (NVIDIA's simulation/robotics teams, Oversonic's Digital Twin
role). Different from web-scale system design too: the focus is throughput/fidelity tradeoffs, data pipelines,
and sim↔real sync, not database sharding.

This chapter comes **after** Chapters 1–3 on purpose: these prompts are far more concrete once you've built
even a small version of one of these systems — practiced cold, they become buzzword-matching instead of
reasoning you can defend under a follow-up question.

## Why it matters

System design is the explicit differentiator at senior level — not a formality. NVIDIA's own interview data
shows coding becomes "pass/fail" at senior+ while system design and judgment carry the real weight. These
prompts map directly to what Chapters 1–3 built, so each one should reference something you actually did.

## Project

Sketch each of these on paper (or in `assets/`), then **narrate it out loud** — record yourself if useful.
Emphasize: throughput vs fidelity tradeoffs, where compute goes (GPU-bound sim vs cloud training vs edge
inference) and why, reproducibility/versioning of sim assets and datasets.

**Primary — simulation-systems design:**
- [ ] Scalable parallel-simulation pipeline (thousands of Isaac Sim/Isaac Gym environments for RL training) —
      GPU utilization, environment resets, throughput vs fidelity tradeoffs *(reference Chapter 3)*
- [ ] Synthetic data generation (SDG) pipeline for training a perception/CV model — domain randomization
      strategy, labeling, dataset versioning, coverage across sim variation
- [ ] Digital twin architecture that stays synchronized with a changing physical asset — sensor ingestion,
      physics-parameter calibration loop, drift detection against real-world telemetry
- [ ] Sim-to-real validation framework — how do you know simulation results will generalize before deploying
      to real hardware *(reference Chapter 2's sim-to-real discussion)*
- [ ] VR/AR teleoperation data-collection pipeline — latency budget from headset/controller to sim or real
      robot, data recording/replay for imitation learning (a genuine differentiator — most candidates won't
      have a ready answer here)

**Secondary — classical robotics** (keep conceptual, don't go deep; Qualcomm's embedded/firmware-leaning role
or Accenture's broader consulting role may still probe this):
- [ ] Sensor fusion pipeline (camera + LiDAR + IMU) with a latency budget *(reference Chapter 1's ROS2 topics)*
- [ ] Real-time control loop constraints
- [ ] Fault-tolerant navigation basics (what happens when a sensor drops out mid-task)

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

Sketches/diagrams go in `04-system-design/assets/`; link them here once drafted.

## Resources

- [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)
- [Robotics interview process across Anduril/Zoox/Boston Dynamics (2026)](https://www.greatrobots.ai/blog/robotics-interview-process-2026)
- [Robotics engineer interview prep guide](https://careersinrobotics.com/guides/robotics-engineer-interview-questions)
