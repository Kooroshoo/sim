# MoveIt

> Status: 🔴 not started

## Concept

MoveIt is the standard motion-planning framework for robotic manipulators (arms) in ROS2 — the manipulation
analog to what Nav2 is for mobile navigation. It answers "given the arm's current joint state and a target
pose, compute a collision-free path through joint space to get there."

## Why it matters

Manipulation-heavy roles (anything touching robot learning for grasping/manipulation, which shows up across
several target postings — Xaba, Accenture Physical AI) assume familiarity with the planning-scene/kinematics
vocabulary MoveIt established as the de facto standard, even in teams that don't use MoveIt itself directly.

## Must-knows for interviews

- **Planning scene**: the world model MoveIt reasons about — the robot's current state plus known obstacles
  (from a point cloud, a CAD model, or manually added collision objects). Planning without an accurate
  planning scene is the single most common cause of "the plan looked fine in simulation but hit something in
  the real world."
- **Forward vs inverse kinematics**: forward kinematics (joint angles → end-effector pose) is a straightforward
  closed-form computation; inverse kinematics (target end-effector pose → joint angles) can have zero, one, or
  infinitely many solutions (redundant manipulators), and is usually solved numerically. Know this asymmetry —
  it's a near-guaranteed interview question for anything manipulation-adjacent.
- **Collision checking**: checking a candidate path against the planning scene for self-collision (arm hitting
  itself) and environment collision (arm hitting the world). This is usually the computational bottleneck in
  motion planning, which is why sampling-based planners (RRT, RRT*) that avoid exhaustively checking every
  point are the default rather than naive grid search.
- **Planning scene updates from perception**: in a real system, the planning scene isn't static — it's updated
  from live sensor data (depth camera → point cloud → octomap). Know this loop exists, even without
  implementing it: perception feeds the planning scene, planning scene feeds motion planning.

## Project

- [ ] Set up a MoveIt planning scene for a simple arm (even a simulated one from an off-the-shelf URDF)
- [ ] Compute forward kinematics for a given joint configuration, then solve inverse kinematics back to it
- [ ] Add a collision object to the scene, replan, observe the path avoid it
- [ ] Deliberately create an unreachable target pose, observe how planning failure is reported

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(screenshots, recordings go here once started)_

## Resources

- [ROS2 docs](https://docs.ros.org/en/rolling/)
