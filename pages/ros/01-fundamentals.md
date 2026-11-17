# ROS2 Fundamentals

> Status: 🔴 not started

## Concept

ROS2's core abstraction is a graph of **nodes** that communicate via **topics** (pub/sub, many-to-many),
**services** (request/response, one-to-one), and **actions** (long-running, goal/feedback/result, cancellable).
Everything else — Gazebo, Nav2, MoveIt — is built on this same communication layer, so getting these
fundamentals solid is what makes the rest of this section make sense instead of feeling like separate tools.

## Why it matters

This is the single most commonly probed ROS2 knowledge area in interviews for simulation/robotics roles —
not because you'll write raw pub/sub code all day, but because QoS mismatches, executor deadlocks, and
lifecycle-node bugs are the actual failure modes interviewers want to know you've internalized, not just used.

## Must-knows for interviews

**Communication patterns**
- **Topics**: many-to-many, fire-and-forget, asynchronous. Use for continuous data streams (sensor readings,
  velocity commands).
- **Services**: one-to-one, synchronous request/response. Use for occasional, quick operations (toggle a
  mode, query a value). Blocking a service call inside a callback is a classic deadlock bug.
- **Actions**: for long-running tasks with feedback (navigate to a goal, execute a grasp). Built on top of
  topics + services internally (goal/cancel services, feedback/status topics) — knowing this decomposition is
  a common follow-up question.

**QoS (Quality of Service) — the thing that trips people up most**
- **Reliability**: `RELIABLE` (guaranteed delivery, retries) vs `BEST_EFFORT` (fire-and-forget, no retries).
  Use `BEST_EFFORT` for high-frequency sensor data (camera, LiDAR) where a dropped frame doesn't matter and
  retries would just add latency; use `RELIABLE` for control commands and anything safety-critical.
- **Durability**: `VOLATILE` (new subscribers get nothing from before they joined) vs `TRANSIENT_LOCAL` (late
  subscribers get the last published message(s) — used for things like static maps or robot description).
- **History & depth**: how many messages to buffer. A mismatch between publisher and subscriber QoS settings
  is a *silent* failure in ROS2 — no error, the subscriber just never receives anything. Knowing this exists
  is the actual interview signal, more than reciting the enum names.

**DDS discovery & the ROS1 → ROS2 story**
- ROS1 had a single master process; ROS2 uses DDS (Data Distribution Service) for fully decentralized,
  peer-to-peer discovery — no single point of failure, but discovery storms/multicast issues are the real-world
  tradeoff, especially on networks that don't play well with multicast (common follow-up: "how would you debug
  nodes that can't find each other?").

**Lifecycle nodes**
- Managed nodes with explicit states: `unconfigured → inactive → active → finalized`, with transition
  callbacks (`on_configure`, `on_activate`, etc.). Used where you need deterministic startup ordering (don't
  start publishing control commands before sensors are configured) — this is standard in Nav2 and MoveIt
  internals.

**Executors**
- `rclcpp::spin()` / `rclpy.spin()` is single-threaded, blocking — fine for a toy node, a real bottleneck the
  moment you have multiple callbacks that shouldn't block each other.
- `MultiThreadedExecutor` runs callbacks concurrently across a thread pool — the production default for any
  node with more than one subscription/timer. Know *why*: a slow callback (e.g. waiting on a service) in a
  single-threaded executor blocks every other callback on that node, including the ones unrelated to it.

**URDF**
- XML robot description: links (rigid bodies), joints (connections + motion type: revolute, prismatic, fixed,
  continuous), visual/collision geometry, inertial properties. This is what Gazebo and MoveIt both consume to
  know what the robot physically looks like and how it moves.

## Code walkthrough

A minimal publisher node, shown in both client libraries since ROS2 supports both equally and robotics teams
mix them (C++ for performance-critical nodes, Python for rapid prototyping/glue code):

<div class="code-tabs">
<div class="code-tabs-nav">
<button class="code-tab-btn active" onclick="simShowTab(this, 'cpp')">C++ (rclcpp)</button>
<button class="code-tab-btn" onclick="simShowTab(this, 'python')">Python (rclpy)</button>
</div>
<div class="code-tab-panel active" data-lang="cpp">

```cpp
{{#include ../../ros/src/controller.cpp:1:25}}
```

</div>
<div class="code-tab-panel" data-lang="python">

```python
{{#include ../../ros/src/controller.py:1:25}}
```

</div>
</div>

Full files live in `ros/src/`.

## Project

- [ ] Write a minimal publisher/subscriber pair in both `rclcpp` and `rclpy`, compare QoS defaults between them
- [ ] Deliberately mismatch QoS between a publisher and subscriber, observe the silent failure
- [ ] Convert a simple node from `rclcpp::spin()` to a `MultiThreadedExecutor`, add a slow callback, show the
      difference
- [ ] Write a minimal URDF for a simple robot (even a 2-wheel differential drive box) and load it in RViz

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|
| | | |

## Results

_(code links, screenshots, recordings go here once started)_

## Resources

- [ROS2 docs](https://docs.ros.org/en/rolling/)
