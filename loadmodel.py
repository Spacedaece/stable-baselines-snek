from stable_baselines3 import PPO
import os
from snakeenv import SnekEnv
import time

env = SnekEnv()
env.reset()

models_dir = f"models/{1687648498}/" #PASTE IN MODEL INT
logdir = f"logs/{1687648498}/"

model_path = f"{models_dir}/194000.zip" #timesteps
model = PPO.load(model_path, env=env)
#tensorboard --logdir=logs

TIMESTEPS = 1000
iters = 0

while True:
	iters += 1
	model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
	model.save(f"{models_dir}/{TIMESTEPS*iters}")

