# sim — Simulation, ROS2 & Robot Learning

Hands-on practice repo for the **simulation/digital-twin engineer** niche (not generalist robotics): 3D
simulation engines + robotics middleware + RL + VR/AR teleoperation. Scope is deliberately narrow — see
"Why this scope" below — and maps directly to what NVIDIA, Oversonic, Xaba, Qualcomm, Accenture Physical AI,
and the Alignerr/Mindrift/Micro1/Toptal remote roles actually ask for.

> Last updated: **17 Nov 2026**

---

## Why this scope

Robotics is too broad a target on its own — SLAM, manipulation, legged locomotion, swarm robotics, aerial
robotics are each their own specialization. This repo stays anchored to the intersection that's actually the
differentiator: **simulation fidelity + sim-to-real/RL + middleware integration + VR/AR**, mirroring the
resume categories (Simulation Engines | Robotics Middleware | Computer Vision & RL | VR/AR) and what target
job postings weight — simulation/RL as primary depth, ROS2 as working fluency to wire things together
(~70/30), not the reverse.

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

## Repo structure

```
sim/
  README.md            — this file: essentials checklist + learning log
  01-ros-gazebo/        — ROS2 + Gazebo: nodes, topics, services, a simple diff-drive robot
  02-rl-mujoco/         — RL fundamentals: PPO/SAC on MuJoCo tasks, easy → hard
  03-isaac-lab/         — scale-up: parallel envs, domain randomization — flagship portfolio project lives here
  notes/                — short concept write-ups (PPO vs SAC, QoS cheatsheet, Kalman derivation)
```

Each experiment folder gets its own mini-README: what was built, what failed first, results, how to run it.
Project-first — code and results, not a documentation website.

### Learning path
1. **ROS2 + Gazebo first** — ROS2 concepts are abstract without a simulator behind them
2. **RL fundamentals in MuJoCo** — fast iteration, no heavy GPU requirement, the standard environment for
   learning PPO/SAC mechanics without fighting simulator tooling
3. **Scale up in Isaac Lab** — once RL fundamentals are solid, port that understanding into GPU-parallelized
   environments; this is also where the flagship portfolio project (Isaac Sim/MuJoCo env → RL policy with
   domain randomization → sim-to-sim or partial sim-to-real demo) lives

---

## 📝 Learning log

| Date | Worked on | What I learned / what failed | Next |
|---|---|---|---|
| | | | |
