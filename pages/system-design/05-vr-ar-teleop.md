# VR/AR Teleoperation Pipeline

> Status: 🔴 not started

## Prompt

Design a data-collection pipeline that uses VR/AR teleoperation to generate robot demonstration data for
imitation learning — a genuine differentiator prompt, since most candidates won't have a ready answer here,
but you have real Meta Quest/OpenXR experience to draw on directly.

## Things to cover when narrating

- **Latency budget**: the full loop from headset/controller motion → tracked pose → mapped robot end-effector
  command → sim or real robot response → visual feedback back to the headset. Name where latency accumulates
  and what budget is tolerable before teleoperation starts feeling unresponsive (this is a direct, concrete
  version of the "real-time constraints" theme that recurs across every system-design prompt in this section).
- **Pose mapping**: controller/hand-tracking pose space doesn't map 1:1 to robot joint space — retargeting
  (scaling, offset, workspace clipping) is required, and gets harder the more the robot's kinematics differ
  from a human arm's.
- **Recording for imitation learning**: what gets logged (observations, actions, timestamps) and in what
  format, so the recorded demonstrations are directly usable as training data for the methods covered in
  [Imitation Learning & VLA](../rl/05-imitation-learning-vla.md) — not just a video, but synchronized
  state-action pairs.
- **Sim vs real teleoperation**: teleoperating in simulation first (cheap, safe, fast iteration on the
  interface itself) before real hardware — and what has to be validated before trusting sim-collected
  demonstrations transfer to real-robot behavior.

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Resources

- [OpenAI Spinning Up](https://spinningup.openai.com/)
