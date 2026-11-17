# Placeholder — replace with the real training script once Chapter 2 is underway.
# Shown in pages/chapter-2.md via: {{#include ../02-rl-mujoco/src/train_ppo.py:1:38}}

from dataclasses import dataclass

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.monitor import Monitor


@dataclass
class TrainConfig:
    task: str = "Ant-v4"
    total_timesteps: int = 1_000_000
    learning_rate: float = 3e-4
    n_envs: int = 4


def make_env(task: str) -> gym.Env:
    env = gym.make(task)
    return Monitor(env)


def train(cfg: TrainConfig) -> PPO:
    env = make_env(cfg.task)
    eval_env = make_env(cfg.task)

    model = PPO(
        "MlpPolicy",
        env,
        learning_rate=cfg.learning_rate,
        verbose=1,
    )

    callback = EvalCallback(eval_env, eval_freq=10_000, best_model_save_path="./best_model")
    model.learn(total_timesteps=cfg.total_timesteps, callback=callback)
    return model


if __name__ == "__main__":
    train(TrainConfig())
