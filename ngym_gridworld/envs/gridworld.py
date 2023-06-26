#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri June 16 15:44:59 2023

@author: molano
"""
import numpy as np
from gym import spaces
import neurogym as ngym
import matplotlib.pyplot as plt


class GridWorld(ngym.TrialEnv):
    """GridWorld task.

    Args:
        cohs: list of float, coherence levels controlling the difficulty of
            the task
        sigma: float, input noise level
        dim_ring: int, dimension of ring input and output
    """
    metadata = {
        'paper_link': '',
        'paper_name': '',
        'tags': ['perceptual', 'navigation', 'gridworld']
    }
    def __init__(self, size=5, start=(0, 0), goal=(4, 4)):
        self.size = size
        self.start = start
        self.goal = goal
        self.observation_space = spaces.Box(-np.inf, np.inf,
                                            shape=(9,), dtype=np.float32)
        self.action_space = spaces.Discrete(5)
        self.rewards = {'correct': 50, 'fail': -1}

    def reset(self):
        self.position = self.start
        return self.position

    def _new_trial(self, **kwargs):
        """
        new_trial() is called when a trial ends to generate the next trial.
        Here you have to set:
        The trial periods: fixation, stimulus...
        Optionally, you can set:
        The ground truth: the correct answer for the created trial.
        """

    def _step(self, action):
        """
        _step receives an action and returns:
            a new observation, obs
            reward associated with the action, reward
            a boolean variable indicating whether the experiment has end, done
            a dictionary with extra information:
                ground truth correct response, info['gt']
                boolean indicating the end of the trial, info['new_trial']
        """
        new_trial = False
        if action == 0:  # Move up
            self.position = (max(self.position[0] - 1, 0), self.position[1])
        elif action == 1:  # Move right
            self.position = (self.position[0], min(self.position[1] + 1, self.size - 1))
        elif action == 2:  # Move down
            self.position = (min(self.position[0] + 1, self.size - 1), self.position[1])
        elif action == 3:  # Move left
            self.position = (self.position[0], max(self.position[1] - 1, 0))

        if self.position == self.goal:
            reward = 50
            new_trial = True
        else:
            reward = -1

        return self.position, reward, False, {'new_trial': new_trial}


    def render(self, render_flag):
            if not render_flag:
                return
            grid = np.zeros((self.size, self.size))
            grid[self.position] = 1  # agent's position marked with 1
            grid[self.goal] = 0.5  # goal position marked with 0.5
            plt.figure(figsize=(5,5))
            plt.imshow(grid, cmap='Pastel1')
            plt.show()


if __name__ == '__main__':
   task = GridWorld()
   task.reset()
   print(task)