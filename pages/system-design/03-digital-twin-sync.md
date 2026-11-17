# Digital Twin Sync Architecture

> Status: 🔴 not started

## Prompt

Design a digital twin that stays synchronized with a changing physical asset over its operational lifetime —
not just an initial CAD-to-sim import, but something that stays accurate as the real system ages/changes.

## Things to cover when narrating

- **Sensor ingestion**: what real-world telemetry feeds back into the twin (joint encoders, force/torque
  sensors, vibration, temperature) and at what rate — this is the actual "sync" mechanism, not a one-time
  import.
- **Physics-parameter calibration loop**: periodically re-estimating simulation parameters (friction, backlash,
  actuator response curves) against real telemetry, since physical systems drift (wear, temperature effects,
  component replacement) in ways a static initial calibration won't capture.
- **Drift detection**: how you'd actually know the twin has diverged from reality — comparing predicted vs
  observed behavior on a held-out set of real operating conditions, and alerting when the divergence exceeds a
  threshold, rather than assuming the twin stays accurate indefinitely.
- **Update cadence tradeoffs**: real-time sync (expensive, often unnecessary) vs periodic recalibration
  (cheaper, introduces lag) — justify a choice based on how fast the physical asset actually changes.

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Resources

- [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)
