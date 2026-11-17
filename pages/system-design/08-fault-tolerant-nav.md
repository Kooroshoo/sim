# Fault-Tolerant Navigation

> Status: 🔴 not started

## Prompt

Design a navigation system that degrades gracefully when a sensor drops out mid-task, rather than failing
outright.

## Things to cover when narrating

- **Detecting the failure**: a sensor that silently stops publishing looks different from one that publishes
  garbage data — both need detection (watchdog timers for the former, plausibility/consistency checks for the
  latter), and neither is caught by "the node is still running."
- **Graceful degradation, not binary fail**: falling back to a reduced-capability mode (e.g. navigate more
  cautiously using only the remaining sensors, reduce max speed) rather than an all-or-nothing stop — ties
  directly to [Nav2](../ros/04-nav2.md)'s recovery-behavior concept (clear costmap, back up, spin, retry)
  generalized to a broader failure-handling philosophy.
- **Redundancy where it's actually justified**: not every sensor needs a backup — reason about which failures
  are safety-critical (justify redundant sensing) vs which just degrade performance (a single sensor plus
  graceful degradation is enough).
- **Recovery vs abort criteria**: explicit conditions for "retry/degrade and continue" vs "this task cannot
  safely continue, abort and request help" — a system that always tries to recover can be more dangerous than
  one that knows when to give up.

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Resources

- [Robotics interview process across Anduril/Zoox/Boston Dynamics (2026)](https://www.greatrobots.ai/blog/robotics-interview-process-2026)
