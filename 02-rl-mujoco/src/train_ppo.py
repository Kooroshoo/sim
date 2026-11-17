# Placeholder — replace with the real training script once Chapter 2 is underway.
# Shown in README.md via: {{#include src/train_ppo.py:1:15}}

import gymnasium as gym
from stable_baselines3 import PPO

def make_env(task: str = "Ant-v4"):
    return gym.make(task)

def train(task: str = "Ant-v4", total_timesteps: int = 1_000_000):
    env = make_env(task)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=total_timesteps)
    return model

if __name__ == "__main__":
    train()
