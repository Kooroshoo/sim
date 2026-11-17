# MuJoCo

> Status: 🔴 not started

## Concept

MuJoCo (Multi-Joint dynamics with Contact) is the standard physics engine for RL research — fast, accurate
contact dynamics, and tightly integrated with Gymnasium, making it the lowest-friction place to actually train
policies rather than fight simulator tooling.

## Why it matters

This is where the Fundamentals page's concepts (PPO vs SAC, reward shaping) stop being abstract and become
something you've actually run — before taking that understanding into the much heavier Isaac Lab tooling.

## Must-knows for interviews

- **MJCF format**: MuJoCo's native XML scene description — bodies, joints, geoms (collision/visual geometry),
  actuators. Conceptually similar to URDF/SDF but MuJoCo-specific; conversion between formats is a real,
  common practical task.
- **Physics stepping**: MuJoCo advances the simulation in discrete timesteps, solving contact constraints each
  step. Know that smaller timesteps = more accurate but slower; too large a timestep causes instability
  (objects tunneling through each other, exploding velocities) — a direct, practical version of the
  fidelity-vs-throughput tradeoff that recurs throughout this entire repo.
- **Contact dynamics**: friction cones, solver iterations, contact softness parameters — the actual physics
  that makes "the robot picks something up" either work or fail to generalize. This is specifically what
  distinguishes MuJoCo's reputation from faster-but-less-accurate alternatives.
- **Gymnasium integration**: the standard `reset()`/`step()`/`observation_space`/`action_space` API that makes
  a MuJoCo environment usable by any off-the-shelf RL library (Stable-Baselines3, CleanRL) without custom glue
  code.

## Project

- [ ] Train PPO on a classic MuJoCo task via Gymnasium (e.g. `Ant-v4`)
- [ ] Deliberately set an unstable timestep, observe the simulation break
- [ ] Move to a harder, contact-rich task once the basics work, compare training difficulty

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(training curves, demo GIFs go here once started)_

## Resources

- [OpenAI Spinning Up](https://spinningup.openai.com/)
