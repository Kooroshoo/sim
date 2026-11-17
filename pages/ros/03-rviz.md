# RViz

> Status: 🔴 not started

## Concept

RViz is the visualization tool for debugging a *running* ROS2 system — not a simulator itself, but the window
into what the robot (real or simulated) thinks is happening: sensor data, coordinate frames, planned paths,
costmaps. If Gazebo is where the robot lives, RViz is how you see what it believes about itself.

## Why it matters

Debugging robotics systems is disproportionately about *visualizing* what's wrong rather than reading logs —
a TF frame drifting, a costmap showing a phantom obstacle, a planned path that clips through a wall. Knowing
RViz fluently is a practical skill that shows up constantly, even though it rarely gets asked about directly
in interviews — it's assumed.

## Must-knows for interviews

- **TF (transform tree)**: the tree of coordinate frame relationships (`base_link → wheel`, `map → odom →
  base_link`), published on `/tf` and `/tf_static`. The `map → odom → base_link` chain specifically is a
  near-universal interview question: `odom` drifts over time (dead reckoning), `map → odom` gets corrected
  periodically by localization — knowing *why* this split exists (not just that it does) is the real signal.
- **Markers**: programmatically drawn visualization primitives (arrows, spheres, line strips) published on a
  topic — how you visualize custom data (a planned trajectory, a detected object's bounding box) that isn't a
  built-in message type RViz already understands.
- **Display plugins**: RobotModel (renders from URDF), LaserScan/PointCloud2, Path, Costmap, Odometry — knowing
  which display type corresponds to which message type is the practical skill of actually using the tool.

## Project

- [ ] Visualize the diff-drive robot from the Gazebo section in RViz via its RobotModel display
- [ ] Add a static TF frame and an odometry-driven frame, observe `map → odom → base_link` directly
- [ ] Publish a custom `Marker` (e.g. a sphere at a "goal" position) and visualize it alongside the robot

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(screenshots, recordings go here once started)_

## Resources

- [ROS2 docs](https://docs.ros.org/en/rolling/)
