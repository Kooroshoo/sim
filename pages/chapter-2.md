# Chapter 2 — RL Fundamentals: Teaching a Policy to Move

> Status: 🔴 not started

## Concept

Reinforcement learning algorithm mechanics (PPO, SAC), reward shaping, and why sim-to-real transfer fails —
learned where iteration is cheap (MuJoCo via Gymnasium), before scaling up to Isaac Lab in Chapter 3. Learning
RL mechanics and heavy simulator tooling at the same time would be fighting two problems at once — this
chapter isolates the first one.

## Why it matters

RL/simulation is the ~70% primary-depth side of this repo's scope (see root README). This is where PPO vs SAC
tradeoffs, reward hacking, and domain randomization stop being interview talking points you memorized and
become things you've actually debugged.

## Project

Train a policy on a classic MuJoCo task (start with something like `Ant-v4` or `Humanoid-v4` via Gymnasium),
then move to a harder contact-rich task once the basics work. Compare PPO vs SAC on the same task.

## Code walkthrough

Keep snippets short — just the lines that illustrate the concept. Full, runnable code lives in
`02-rl-mujoco/src/`.

```
{{#include ../02-rl-mujoco/src/train_ppo.py:1:15}}
```

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(reward curves, demo GIFs, PPO vs SAC comparison go here once started)_

## Resources

- [OpenAI Spinning Up](https://spinningup.openai.com/)
- [Sutton & Barto (free)](http://incompleteideas.net/book/the-book.html)

