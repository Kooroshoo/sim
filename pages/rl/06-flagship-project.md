# Flagship Project

> Status: 🔴 not started

## Concept

The capstone project this entire repo builds toward: an Isaac Sim/Isaac Lab environment, an RL policy trained
on it with domain randomization, and a sim-to-sim (or ideally partial sim-to-real) demonstration — documented
well enough to be a concrete, narratable "walk me through a project" story.

## Why it matters

This single project is the concrete answer to the most common senior-level interview question ("tell me about
something you built"), and it's literally the expertise graded on Alignerr, Mindrift, and Toptal applications
from the remote-roles list — the same project pays off in both the Italy job search and the remote-roles
track.

## Project

- [ ] Pick one task (manipulation, locomotion, or navigation) — finishable, not the most ambitious option
- [ ] Build/configure the Isaac Lab environment
- [ ] Train a baseline policy (PPO or SAC, reusing what the Fundamentals/MuJoCo pages taught)
- [ ] Add domain randomization (see [Sim-to-Real Transfer](./04-sim-to-real.md)), show before/after robustness
- [ ] Write up: problem, approach, what failed first, what changed, results
- [ ] Publish on GitHub + a short post (LinkedIn or blog)

## Code walkthrough

```python
{{#include ../../rl/src/env_config.py:1:38}}
```

Full file lives in `rl/src/`.

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Results

_(reward curves, domain randomization before/after, sim-to-real demo go here once started)_

## Resources

- [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)
