# Chapter 3 — Scaling Up: Isaac Lab, Domain Randomization & Sim-to-Real

> Status: 🔴 not started

## Concept

Porting RL understanding from Chapter 2 into GPU-parallelized environments (Isaac Lab), adding domain
randomization, and reasoning honestly about the sim-to-real gap. This is also where the **flagship portfolio
project** lives: Isaac Sim/Isaac Lab environment → RL policy with domain randomization → sim-to-sim or
(ideally) partial sim-to-real demo.

## Why it matters

This chapter is the direct match to what NVIDIA's own postings name explicitly (Isaac Lab, CUDA/warp, GPU-
accelerated RL), and it's the concrete "walk me through a project" story for interviews — and literally the
expertise graded on Alignerr/Mindrift/Toptal applications.

## Project

- [ ] Pick one task (manipulation, locomotion, or navigation) — finishable, not the most ambitious option
- [ ] Build/configure the Isaac Lab environment
- [ ] Train a baseline policy (PPO or SAC, reusing what Chapter 2 taught)
- [ ] Add domain randomization, show before/after robustness
- [ ] Write up: problem, approach, what failed first, what changed, results
- [ ] Publish on GitHub + a short post (LinkedIn or blog)

## Code walkthrough

Keep snippets short — just the lines that illustrate the concept. Full code lives in `03-isaac-lab/src/`.

```
{{#include ../03-isaac-lab/src/env_config.py:1:15}}
```

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(reward curves, domain randomization before/after, sim-to-real demo go here once started)_

## Resources

- [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)

