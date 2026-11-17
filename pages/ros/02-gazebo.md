# Gazebo

> Status: 🔴 not started

## Concept

Gazebo (`gz-sim`, the modern rewrite — not "Gazebo Classic") is the physics simulator that gives ROS2 concepts
something real to act on: a robot model with actual sensors publishing to actual topics, actuators that
respond to actual commands, and a physics engine underneath that makes the whole thing behave plausibly.

## Why it matters

This is the bridge between "I know ROS2 syntax" and "I can get a simulated robot actually doing something" —
which is the first checkpoint of this entire repo's learning path, and the thing most interview take-homes in
this space actually ask you to demonstrate.

## Must-knows for interviews

- **Worlds (SDF)**: the scene description format — static geometry, lighting, physics parameters (gravity,
  solver iterations), and model/plugin references. Distinct from URDF (robot-only) — SDF describes the whole
  world, URDF describes one robot (and can be converted to/embedded as SDF).
- **Plugins**: C++ shared libraries that hook into the simulation loop — sensor plugins (camera, LiDAR, IMU),
  actuator/controller plugins (diff-drive, joint controllers). Know that "the sensor doesn't exist until a
  plugin says it does" — a common point of confusion for people coming from "it's just physics" intuitions.
- **The `ros_gz` bridge**: Gazebo's own transport layer is *not* ROS2 topics — `ros_gz_bridge` translates
  between Gazebo transport messages and ROS2 topics (configurable per-topic, per-direction). Forgetting to
  bridge a topic is the most common "why can't I see my sensor data in ROS2" bug.
- **Spawning and inspecting**: spawning a model into a running world, then using `ros2 topic list` / `ros2
  topic echo` / `ros2 topic hz` to verify what's actually being published and at what rate — the first thing
  to do when debugging "nothing's happening."

## Project

- [ ] Build a simple diff-drive robot (box chassis + two wheels), spawn it in an empty Gazebo world
- [ ] Add a LiDAR or camera sensor plugin, bridge it to ROS2, verify with `ros2 topic echo`
- [ ] Publish velocity commands from a ROS2 node, confirm the robot moves in the simulated world
- [ ] Deliberately forget to bridge a topic, observe and diagnose the failure mode

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(code links, screenshots, recordings go here once started)_

## Resources

- [ROS2 docs](https://docs.ros.org/en/rolling/)
