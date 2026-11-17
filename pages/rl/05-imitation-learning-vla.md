# Imitation Learning & VLA

> Status: 🔴 not started

## Concept

Imitation learning trains a policy directly from demonstrations (expert trajectories) instead of trial-and-
error reward maximization — behavior cloning is the simplest form (supervised learning: observation → expert
action). Vision-Language-Action (VLA) models extend this idea to large, multimodal foundation models that
take vision and language instructions as input and output robot actions directly — the current direction the
field is actually moving, and it came up repeatedly across target postings (NVIDIA, Amazon, STMicroelectronics)
while researching this repo's job targets.

## Why it matters

This is the newest, fastest-moving part of the field, and specifically where your VR/AR teleoperation
experience (Meta Quest, OpenXR) becomes a genuine differentiator — teleoperation is one of the main ways
demonstration data actually gets collected for these methods.

## Must-knows for interviews

- **Behavior cloning**: the simplest imitation learning approach — supervised learning directly from
  (observation, expert action) pairs. Know its core weakness: **distribution shift / compounding error** — the
  policy makes small mistakes, ends up in states the expert demonstrations never covered, and has no signal
  for what to do there, so errors compound over the episode. This is the single most important behavior-
  cloning concept to be able to explain.
- **DAgger and related fixes**: iteratively collecting more expert labels on states the trained policy
  actually visits (not just the original demonstration states) — a direct answer to the distribution-shift
  problem above.
- **Diffusion policies**: representing the action distribution with a diffusion model instead of a direct
  regression — handles multimodal action distributions well (there are often multiple valid ways to perform a
  task, and plain regression tends to average between them into an invalid action; diffusion models can
  represent "either of these is fine" instead of blending them into something that's neither).
- **Vision-Language-Action (VLA) models**: foundation models (often built on top of a vision-language model
  backbone) that take an image + a language instruction and directly output robot actions — the pitch is
  generalization across tasks and embodiments from internet-scale pretraining plus robot demonstration data,
  rather than training a narrow policy per task from scratch.
- **Where teleoperation fits in**: VR/AR teleoperation (controller or hand tracking mapped to robot end-
  effector commands) is a primary way to collect the demonstration data these methods need at scale — this is
  the direct link back to [VR/AR Teleoperation](../system-design/05-vr-ar-teleop.md) and your existing Meta
  Quest/OpenXR experience.

## Project

- [ ] Collect a small set of demonstrations (even scripted/synthetic ones) for a simple task
- [ ] Train a behavior-cloning policy, deliberately show it a held-out state it's never seen, observe the
      compounding-error failure mode directly
- [ ] Read (don't necessarily implement) one VLA paper and write a short summary of how it differs from a
      standard RL policy architecture

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Results

_(demo GIFs, comparisons go here once started)_

## Resources

- [Sutton & Barto (free)](http://incompleteideas.net/book/the-book.html)
