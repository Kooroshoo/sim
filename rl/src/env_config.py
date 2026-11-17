# Placeholder — replace with the real env config once Chapter 3 is underway.
# Shown in pages/chapter-3.md via: {{#include ../03-isaac-lab/src/env_config.py:1:38}}

from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.managers import EventTermCfg, ObservationTermCfg, RewardTermCfg
from isaaclab.utils import configclass


@configclass
class RandomizationCfg:
    """Domain randomization applied at the start of each episode."""

    friction_range: tuple[float, float] = (0.6, 1.2)
    mass_range: tuple[float, float] = (0.85, 1.15)
    push_robot: EventTermCfg = EventTermCfg(
        func="push_by_setting_velocity",
        mode="interval",
        interval_range_s=(5.0, 10.0),
    )


@configclass
class FlagshipEnvCfg(ManagerBasedRLEnvCfg):
    """Base config for the flagship portfolio-project environment.

    Fill in: scene, observations, actions, rewards, terminations, and the
    domain-randomization event manager once the task is chosen.
    """

    num_envs: int = 4096
    env_spacing: float = 2.5
    episode_length_s: float = 20.0

    randomization: RandomizationCfg = RandomizationCfg()

    def __post_init__(self):
        super().__post_init__()
        self.sim.dt = 1 / 120
        self.decimation = 2
