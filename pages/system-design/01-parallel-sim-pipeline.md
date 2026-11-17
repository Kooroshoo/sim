# Scalable Parallel-Simulation Pipeline

> Status: 🔴 not started

## Prompt

Design a system that trains an RL policy using thousands of parallel simulation environments (Isaac Lab-style)
— cover environment management, GPU utilization, and data flow from simulation to policy update.

## Things to cover when narrating

- **Environment batching**: thousands of environment instances stepped simultaneously on GPU rather than one
  at a time on CPU — the core throughput lever. Reference your own experience from
  [Isaac Lab](../rl/03-isaac-lab.md) if you've built even a small version.
- **Reset handling**: individual environments finish episodes at different times — the design needs to reset
  and re-seed finished environments without stalling the ones still running, or you lose most of the
  parallelism advantage.
- **Throughput vs fidelity tradeoff**: more environments at lower per-step fidelity (simpler collision
  geometry, fewer physics substeps) vs fewer environments at higher fidelity — explicitly name this tradeoff
  and justify a choice for a stated goal (e.g. "early-stage policy search" favors throughput, "final validation
  before hardware deployment" favors fidelity).
- **Data flow**: how observations/rewards batch back to the learning algorithm, and where the bottleneck
  actually sits (usually GPU memory for environment count, not CPU, once the environments themselves are
  GPU-resident).

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Resources

- [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)
