import gym
from gym import spaces
from stable_baselines3.common.env_checker import check_env #stablebaselines3 only
from snakeenv import SnekEnv
env = SnekEnv()
# It will check your custom environment and output additional warnings if needed
check_env(env)