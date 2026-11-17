# System Design — Simulation & Robotics Systems

Not classical robotics system design (fleet management, autonomy stacks) — **simulation-systems design**,
since that's what your actual target roles probe (NVIDIA's simulation/robotics teams, Oversonic's Digital Twin
role). This section comes **after** [ROS](../ros/index.md) and [RL](../rl/index.md) on purpose: these prompts
are far more concrete once you've built even a small version of one of these systems — practiced cold, they
become buzzword-matching instead of reasoning you can defend under a follow-up question.

## How to practice these

Sketch each one on paper (or in `system-design/assets/`), then **narrate it out loud** — record yourself if
useful. Emphasize: throughput vs fidelity tradeoffs, where compute goes (GPU-bound sim vs cloud training vs
edge inference) and why, reproducibility/versioning of sim assets and datasets.

## Primary — simulation-systems design

- [Scalable Parallel-Simulation Pipeline](./01-parallel-sim-pipeline.md)
- [Synthetic Data Generation Pipeline](./02-sdg-pipeline.md)
- [Digital Twin Sync Architecture](./03-digital-twin-sync.md)
- [Sim-to-Real Validation Framework](./04-sim-to-real-validation.md)
- [VR/AR Teleoperation Pipeline](./05-vr-ar-teleop.md)

## Secondary — classical robotics

Keep these conceptual, don't go deep — some interviewers (Qualcomm's embedded/firmware-leaning role, or
Accenture's broader consulting role) may still probe this.

- [Sensor Fusion Pipeline](./06-sensor-fusion.md)
- [Real-Time Control Loops](./07-real-time-control.md)
- [Fault-Tolerant Navigation](./08-fault-tolerant-nav.md)
