# Sim-to-Real Transfer

> Status: 🔴 not started

## Concept

The sim-to-real gap: a policy trained entirely in simulation performs worse — sometimes dramatically worse —
when deployed on real hardware, because simulation is never a perfect model of reality. This page is about
*why* that gap exists and what's actually done about it, not just that it's a known hard problem.

## Why it matters

"Why does sim-to-real transfer fail?" is close to a guaranteed interview question for any simulation/RL role,
and "it's just hard" is not an answer that distinguishes you from anyone else who's heard the term. Being able
to name the specific failure modes and mitigations is the actual signal.

## Must-knows for interviews

- **Where the gap actually comes from**:
  - *Dynamics mismatch*: simulated physics (friction, contact, actuator response, mass distribution) never
    exactly matches the real robot — small errors compound over an episode.
  - *Perception mismatch*: simulated sensor data (camera images, LiDAR returns) looks different from real
    sensor data — lighting, noise characteristics, lens artifacts the simulator doesn't model.
  - *Latency/timing mismatch*: real control loops have communication delays, actuator response times, and
    jitter that a simulation often idealizes away.
  - *Unmodeled real-world variation*: real environments have clutter, wear, and edge cases that a simulation's
    authored scenes simply don't include.
- **Domain randomization as the primary mitigation**: randomize the parameters you're uncertain about
  (friction, mass, sensor noise, textures, lighting) across training so the policy learns to be robust to
  variation rather than overfitting to one exact simulated configuration — the implicit bet is that the real
  world will fall somewhere inside the randomized range.
- **System identification as the complementary approach**: instead of (or in addition to) randomizing broadly,
  measure the real system's actual parameters and calibrate the simulation to match more precisely — narrower,
  more accurate randomization around a well-measured center point, rather than wide randomization around a
  guess.
- **Validating transfer before deploying**: comparing simulated sensor outputs, kinematics, and dynamics
  against logged real-world data *before* running a policy on real hardware — this is exactly the
  [Sim-to-Real Validation Framework](../system-design/04-sim-to-real-validation.md) system-design prompt, and
  this page is the conceptual grounding for that design discussion.

## Project

- [ ] Take a policy trained in the MuJoCo or Isaac Lab sections, deliberately perturb one physics parameter at
      test time (friction, mass) that wasn't randomized during training, observe the failure
- [ ] Re-train with that parameter randomized, compare robustness
- [ ] Write a short note on which failure mode (dynamics, perception, latency, unmodeled variation) each
      change actually addressed

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(before/after robustness comparisons go here once started)_

## Resources

- [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)
