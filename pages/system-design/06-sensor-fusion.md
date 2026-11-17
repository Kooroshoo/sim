# Sensor Fusion Pipeline

> Status: 🔴 not started

## Prompt

Design a sensor fusion pipeline combining camera, LiDAR, and IMU data, with a stated latency budget.

## Things to cover when narrating

- **Why fuse at all**: each sensor has complementary failure modes — camera gives rich semantic information
  but poor depth/range accuracy and fails in low light; LiDAR gives accurate range but no semantic/color
  information and struggles with transparent/reflective surfaces; IMU gives high-rate motion estimates but
  drifts without correction. Fusion compensates for each sensor's individual weaknesses.
- **Synchronization**: sensors run at different rates (IMU often 100s of Hz, camera/LiDAR tens of Hz) and have
  different latencies — timestamping and interpolation/extrapolation strategy to align them matters more in
  practice than the fusion algorithm itself.
- **Fusion approach**: Extended Kalman Filter (EKF) as the standard baseline — know roughly how it works
  (predict step using motion model, update step using sensor measurements, weighted by uncertainty) well
  enough to sketch it, even if a production system uses something more sophisticated.
- **Latency budget**: name an actual number and justify it against the control loop rate the fused estimate
  feeds into — a sensor fusion pipeline accurate but too slow for the downstream controller is a wrong design.

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Resources

- [kalmanfilter.net](https://www.kalmanfilter.net/)
