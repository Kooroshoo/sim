# Isaac Lab

> Status: 🔴 not started

## Concept

Isaac Lab is NVIDIA's lightweight, GPU-parallelized robot-learning framework built on top of Isaac Sim —
instead of running one environment at a time (as in MuJoCo/Gymnasium), it runs thousands of environment
instances in parallel on the GPU, turning weeks of training into hours. This is where RL understanding from
the Fundamentals and MuJoCo pages gets scaled up to match what production robot-learning pipelines actually
look like.

## Why it matters

This is the single most explicit match to what NVIDIA's own postings name (Isaac Lab, CUDA/warp, GPU-
accelerated RL) — and it's where the **flagship portfolio project** lives.

## Must-knows for interviews

- **Isaac Sim vs Isaac Lab, the distinction cold**: Isaac Sim is the full high-fidelity simulation platform
  (built on Omniverse/USD) — photorealistic rendering, synthetic data generation (SDG), SIL/HIL testing. Isaac
  Lab is a lightweight framework *built on top of* Isaac Sim, specifically optimized for robot-learning
  workflows (RL, imitation learning, motion planning) — you don't need Isaac Sim's full rendering pipeline
  running at full fidelity to train a policy efficiently. Confusing these two in an interview is an immediate,
  obvious knowledge gap.
- **GPU-accelerated parallel simulation**: thousands of environment instances stepped simultaneously on the
  GPU (the lineage traces back to Isaac Gym). The practical consequence: training throughput is usually
  GPU-memory-bound (how many environments fit) rather than CPU-bound, which changes how you think about
  scaling a training run.
- **USD basics**: Universal Scene Description, the scene format Isaac Sim/Omniverse builds on — composable,
  layered scene graphs. Most digital-twin roles assume at least passing USD familiarity.
- **Domain randomization**: randomizing physics parameters (friction, mass, actuator strength), visual
  appearance (textures, lighting), and sensor noise across parallel environment instances during training, so
  the learned policy doesn't overfit to the exact simulated physics/appearance — see the
  [Sim-to-Real Transfer](./04-sim-to-real.md) page for why this is the main lever against the sim-to-real gap.

## Project

This is also where the **flagship portfolio project** lives — see [Flagship Project](./06-flagship-project.md)
for the full milestone breakdown. Subsection-specific practice first:

- [ ] Get a minimal Isaac Lab environment running, confirm parallel environment stepping works
- [ ] Port the PPO understanding from the Fundamentals/MuJoCo pages into an Isaac Lab training loop
- [ ] Add domain randomization to one parameter (e.g. friction range), observe policy robustness before/after

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(training curves, domain randomization before/after comparisons go here once started)_

## Resources

- [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)
