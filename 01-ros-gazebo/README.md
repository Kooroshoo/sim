# Chapter 1 — ROS2 + Gazebo: Giving Simulation a Voice

> Status: 🔴 not started

## Concept

ROS2 concepts (nodes, topics, QoS, lifecycle) are abstract without something real behind them. Gazebo (`gz-sim`)
gives a simulated robot with actual sensors publishing to actual topics, so every concept below gets practiced
against something concrete instead of memorized in the abstract.

## Why it matters

ROS2 is the "working fluency" ~30% of this repo's scope — enough to wire simulation to middleware and talk
credibly about it in interviews (Alignerr's closest-matching posting explicitly lists "integrate simulations
with ROS2" as a required skill). Not the primary depth target — that's RL/simulation in later chapters.

## Project

Build a simple diff-drive robot in Gazebo, write ROS2 nodes to:
- Spawn the robot and inspect its topics (`ros2 topic list`, `ros2 topic echo`)
- Subscribe to a sensor topic (LiDAR or camera) and do something with the data
- Publish velocity commands to drive it toward a goal
- Visualize in `rviz2`

## Code walkthrough

Keep snippets short — just the lines that illustrate the concept. Full, compiling code lives in `src/`.

```
{{#include src/controller.cpp:1:15}}
```

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(code links, screenshots, recordings go here once started)_

## Resources

- [ROS2 docs](https://docs.ros.org/en/rolling/)
