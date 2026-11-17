# Placeholder — replace with the real env config once Chapter 3 is underway.
# Shown in README.md via: {{#include src/env_config.py:1:15}}

from isaaclab.envs import ManagerBasedRLEnvCfg
from isaaclab.utils import configclass

@configclass
class FlagshipEnvCfg(ManagerBasedRLEnvCfg):
    """Base config for the flagship portfolio-project environment.

    Fill in: scene, observations, actions, rewards, terminations, and the
    domain-randomization event manager once the task is chosen.
    """

    num_envs: int = 4096
    env_spacing: float = 2.5
