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

PPO Model Reinforcement Learning
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




