# Real-Time Control Loops

> Status: 🔴 not started

## Prompt

Design (or reason about) a real-time control loop for a robot, covering the timing constraints that make
"real-time" mean something specific rather than just "fast."

## Things to cover when narrating

- **What "real-time" actually means**: not "fast" but "deterministic" — a hard real-time system must meet its
  deadline every single cycle, or the consequence is a correctness failure, not just a slowdown. Soft
  real-time tolerates occasional missed deadlines with degraded (not catastrophic) results. Know which one a
  given control loop (e.g. a balance controller vs a path-planning request) actually needs.
- **Where jitter comes from**: OS scheduling (a non-real-time OS can preempt your control thread at an
  inconvenient moment), communication latency (network/DDS discovery overhead — ties back to
  [ROS2 Fundamentals](../ros/01-fundamentals.md)), and computation time variance (a planner that sometimes
  takes 2ms and sometimes 20ms is a jitter source even if the average is fine).
- **Mitigations**: dedicated real-time threads/priorities, bounding worst-case computation time rather than
  just optimizing average case, and decoupling "must run every cycle, deterministically" logic (e.g. a safety
  watchdog) from "can be slower, best-effort" logic (e.g. high-level planning).

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Resources

- [ROS2 docs](https://docs.ros.org/en/rolling/)
