# RL — Reinforcement Learning for Robotics

This is the primary-depth ~70% of this repo's scope (see root README "Why this scope") — the intersection of
simulation, learning, and sim-to-real transfer that your target roles (NVIDIA, Oversonic, Alignerr/Mindrift)
actually weight most heavily.

## Learning path

Learn RL algorithm mechanics where iteration is cheap (MuJoCo), before scaling up to GPU-parallelized
environments (Isaac Lab). Doing both at once means fighting two hard problems simultaneously — this section
isolates them.

## Subsections

- [Fundamentals](./01-fundamentals.md) — MDPs, PPO vs SAC, reward shaping, the actual algorithm mechanics
- [MuJoCo](./02-mujoco.md) — MJCF format, physics stepping, Gymnasium integration
- [Isaac Lab](./03-isaac-lab.md) — GPU-parallel environments, domain randomization
- [Sim-to-Real Transfer](./04-sim-to-real.md) — why the gap exists and how it's mitigated
- [Imitation Learning & VLA](./05-imitation-learning-vla.md) — behavior cloning, diffusion policies,
  Vision-Language-Action models
- [Flagship Project](./06-flagship-project.md) — the portfolio project this whole section builds toward
