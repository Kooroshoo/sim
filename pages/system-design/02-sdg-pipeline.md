# Synthetic Data Generation Pipeline

> Status: 🔴 not started

## Prompt

Design a pipeline that generates synthetic training data for a perception/computer-vision model, using a
simulator as the data source.

## Things to cover when narrating

- **Domain randomization strategy for perception**: randomizing textures, lighting, camera pose/intrinsics,
  and object placement — distinct from the *physics* domain randomization covered in
  [Sim-to-Real Transfer](../rl/04-sim-to-real.md); here the randomization target is visual realism gap, not
  dynamics mismatch.
- **Automatic labeling**: the actual advantage of synthetic data over real — ground-truth labels (segmentation
  masks, bounding boxes, depth) come for free from the simulator instead of requiring manual annotation.
- **Dataset versioning and coverage**: tracking which randomization ranges/scene configurations were used to
  generate a given dataset version, and reasoning about *coverage* — does the randomization range actually
  span the variation the model will see in deployment, or does it just look varied without covering the right
  axes of variation?
- **Validation against real data**: a held-out set of real images to check the synthetic-trained model
  actually generalizes, not just that it performs well on more synthetic data from the same generator.

## Log

| Date | What I tried | What failed / what I learned |
|---|---|---|

## Resources

- [Isaac Lab docs](https://developer.nvidia.com/isaac/lab)
