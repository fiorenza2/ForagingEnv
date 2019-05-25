import gym
from gym import spaces
import numpy as np

class ForagingEnv(gym.Env):
    def __init__(self):
        self._seed = 0
        self.actions = [0,1,2,3]

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.MultiBinary(3)

        self.locs = ['left','right']

    def step(self, action):
        if action == 0:
            self.state = 0
            return ([0,0,0], 0, False, {})
        elif action == 1:
            self.state = 1
            if self.loc == 'left':
                return ([0,1,0], 0, False, {})
            elif self.loc == 'right':
                return ([0,0,1], 0, False, {})
        elif action == 2:
            self.state = 2
            if self.loc == 'left':
                return ([1,0,0], 3, True, {})
            else:
                return ([0,0,0], -3, True, {})
        elif action == 3:
            self.state = 3
            if self.loc == 'right':
                return ([1,0,0], 3, True, {})
            else:
                return ([0,0,0], -3, True, {})
    
    def reset(self):
        self.loc = self.locs[np.random.binomial(1,0.5)]
        self.state = 0
    
    def render(self, mode='human'):
        if mode == 'human':
            return self.state
