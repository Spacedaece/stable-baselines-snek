import gym
from gym import spaces
import numpy as np
import cv2
import random
import time
from collections import deque

SNAKE_LEN_GOAL = 30
# Reconfigurable Intelligent Surface:
def collision_with_apple(apple_position, score): #defines game rules
    apple_position = [random.randrange
                      
                      (1,50)*10,random.randrange(1,50)*10]
    score += 1
    return apple_position, score

def collision_with_boundaries(snake_head):
    if snake_head[0]>=500 or snake_head[0]<0 or snake_head[1]>=500 or snake_head[1]<0 :
        return 1
    else:
        return 0

def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0
#-------------------------------------------------------------------------------      
class SnekEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self):
    super(SnekEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:
    self.action_space = spaces.Discrete(4) # 4 possible actions for our snake (up/down/left/right)
    # Example for using image as input:
    self.observation_space = spaces.Box(low=-500, high=500,
                                        shape=(5+SNAKE_LEN_GOAL,), dtype=np.float32) #CHANGE vector of values, goal + other traits, add comma
    self.reward = 0
 
  def step(self, action):
    
    self.prev_actions.append(action)
    cv2.imshow('a',self.img)
    cv2.waitKey(1)
    self.img = np.zeros((500,500,3),dtype='uint8')  
    # Display Apple
    cv2.rectangle(self.img,(self.apple_position[0],self.apple_position[1]),(self.apple_position[0]+10,self.apple_position[1]+10),(0,0,255),3)
    # Display Snake
    for position in self.snake_position: #position is temp variable 
        cv2.rectangle(self.img,(position[0],position[1]),(position[0]+10,position[1]+10),(0,255,0),3)
    
    # Takes step after fixed time
    t_end = time.time() + 0.05
    k = -1
    while time.time() < t_end:
        if k == -1:
            k = cv2.waitKey(1)
        else:
            continue
            
    # 0-Left, 1-Right, 3-Up, 2-Down, q-Break
    # a-Left, d-Right, w-Up, s-Down

    
    # Change the head position based on the button direction
    if action == 1:
        self.snake_head[0] += 10
    elif action == 0:
        self.snake_head[0] -= 10
    elif action == 2:
        self.snake_head[1] += 10
    elif action == 3:
        self.snake_head[1] -= 10

    apple_reward = 0
    # Increase Snake length on eating apple
    if self.snake_head == self.apple_position:
        self.apple_position, self.score = collision_with_apple(self.apple_position, self.score)
        self.snake_position.insert(0,list(self.snake_head))
        apple_reward = 10000 #short-term reward for eating apple (greater than 250)
    else: #apple reward adds to temp reward
        self.snake_position.insert(0,list(self.snake_head))
        self.snake_position.pop()
     
    # On collision kill the snake and print the score
    if collision_with_boundaries(self.snake_head) == 1 or collision_with_self(self.snake_position) == 1:
        font = cv2.FONT_HERSHEY_SIMPLEX
        self.img = np.zeros((500,500,3),dtype='uint8')
        cv2.putText(self.img,'Your Score is {}'.format(self.score),(140,250), font, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('a',self.img)
        self.done = True
    
    euclidean_dist_to_apple = np.linalg.norm(np.array(self.snake_head) - np.array(self.apple_position))
    # punishes for distance from apple
    self.total_reward = ((250 - euclidean_dist_to_apple) + apple_reward)/100 # offsets the adversion to living (250 as canvas is 500x500)
    print(self.total_reward)

    self.reward = self.total_reward - self.prev_reward
    self.prev_reward = self.total_reward # new previous award
    #REWARD
    if self.done: #NEW CHANGE
        self.total_reward = -10 #if killed, severely punish bot

    #observation
    head_x = self.snake_head[0]
    head_y = self.snake_head[1]
    apple_delta_x =  self.apple_position[0] - head_x #distance?
    apple_delta_y = self.apple_position[1] - head_y
    snake_length = len(self.snake_position) #in 10-wide units   

    # observation must be fixed size as snake length increases by one
    self.observation = [head_x, head_y, apple_delta_x, apple_delta_y, snake_length]+ list(self.prev_actions) #previous actions for positioning rest of body
    self.observation = np.array(self.observation)


    return self.observation, self.total_reward, self.done
#-------------------------------------------------------------------------------  
  def reset(self): # Function gets called second after init 
    """resets or inilizations the environment for each new model episode"""
    self.done = False #when environment is reset self.done is true
    self.img = np.zeros((500,500,3),dtype='uint8')
    # Initial Snake and Apple position
    self.snake_position = [[250,250],[240,250],[230,250]] #inital snake position, there are three segments
    self.apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10] #inital apple position
    self.score = 0 #score
    self.prev_button_direction = 1 #previous buttion direction
    self.button_direction = 1 #determines inital direction
    self.snake_head = [250,250]

    self.prev_reward = 0
    #head_x, head_y,apple_x, apple_y, snake_length, previous moves (aware of body, passing entire self.image is redundant)
    #where is head of snake, long, and apple (ai can extrapolate rest of snake)

    head_x = self.snake_head[0] 
    head_y = self.snake_head[1]
    apple_delta_x = self.apple_position[0] - head_x  #distance?
    apple_delta_y = self.apple_position[1] - head_y
    snake_length = len(self.snake_position) #in 10-wide units
    
    self.prev_actions = deque(maxlen = SNAKE_LEN_GOAL)
    for _ in range(SNAKE_LEN_GOAL):
       self.prev_actions.append(-1) 

    self.observation = [head_x, head_y, apple_delta_x, apple_delta_y, snake_length]+ list(self.prev_actions) #helps to pinpoint the observation
    self.observation = np.array(self.observation)
    return self.observation  # reward, done, info can't be included
#-------------------------------------------------------------------------------     
    def render(self, mode='human'):
        pass
    def close(self):
        pass
