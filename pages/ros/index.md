# ROS — Robot Operating System

The middleware layer: how perception, planning, and control components talk to each other and to simulation.
This section covers ROS2 itself plus the libraries built on top of it that interviewers actually ask about —
Gazebo for simulation, RViz for visualization, Nav2 for navigation, and MoveIt for manipulation.

Scope reminder (see root README "Why this scope"): this is "working fluency," not the primary depth target of
this repo — enough to wire simulation to middleware and talk credibly about it in interviews. The primary
depth investment is in [RL](../rl/index.md).

## Subsections

- [Fundamentals](./01-fundamentals.md) — nodes, topics, services, actions, QoS, DDS, lifecycle nodes,
  executors, URDF
- [Gazebo](./02-gazebo.md) — simulation: worlds, plugins, sensors, the `ros_gz` bridge
- [RViz](./03-rviz.md) — visualization: markers, TF frames, debugging a running system
- [Nav2](./04-nav2.md) — navigation stack: costmaps, planners, controllers, behavior trees, recovery
- [MoveIt](./05-moveit.md) — manipulation: planning scenes, kinematics, collision checking
