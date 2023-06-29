# stable-baselines-snek


Snake
Iteration of the classic snake game in python

Actions

    4 distinct actions taken by player
    (up, down, left, right)
    Player (snake) cannot stop, only change direction
    Direction can only change consecutively (no left-right or up-down)

Failure

    Running into itself, crashing into game boundaries

Objective

    Game begins with player having a 3-segment snake traveling right
    Gaining one segment via colliding w/ “apples” (red particles randomly generated after each collision)
    Only one apple exists at one time, regenerates every time the player consumes it.

Scoring
    
    For every segment added after the inital beginning, score increases by 1
    ex. 8 segments, score is 5

Running Reinforcement Learning Models
Prerequisites
    
    Windows 10 or Linux Recommended
    Python 3.7+ and Pytorch >3.11
    Anaconda Navigator recommended (VS Code or Pycharm)
    Tensorboard
    

Installation

    Within Anaconda Navigator, launch your desired application.
    Within your application, setting up a virtual environment is highly recommended to keep your files in one place. For more infomation, visit "https://code.visualstudio.com/docs/python/environments" 
    Name your environment with your specified name.
    To install, run "pip install stable-baselines3[extra]" in the terminal within your environment.
    Install Tensorboard at "https://anaconda.org/conda-forge/tensorboard"
    Install your files into your environment's folder. Visit "https://pythonprogramming.net/introduction-reinforcement-learning-stable-baselines-3-tutorial/" for more info.

Testing

    Run "createmodel.py" to create a new model with PPO. Feel free to modify the model's parameters to your desire.
    Within your terminal, run "tensorboard --logdir=logs." Click on the link given at the end of the output message to see your model's progress
    
    To load an existing model, go to "loadmodel.py"
    With tensorboard or file explore at "YOURENV/models", see which model to run
    In these lines, replace MODELNAME with desired model name as an integer only
    models_dir = f"models/{MODELNAME}/" 
    logdir = f"logs/{MODELNAME}/"

    
Model Environment Overview
Environment 
    
    Actions based on observations 
    (body length, distance from apple, head position, apple position)
     Storing previous actions determines body position (accounting for turns)

Rewards
    
    Rewards based on distance to apple and failure
    (running into walls, into itself)
    Punishment
    Calculating euclidean distance to apple 
    Deducting rewards based on increasing distance to apple
    Deducts rewards if killed (running into wall/itself)
    Rewards
    Consuming apple gives a short-term reward boost




