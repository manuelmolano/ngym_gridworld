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
    def __init__(self, dt=100, size=5, start=(0, 0),
                 goal=(4, 4), obstacles=None):
        super().__init__(dt=dt)
        self.size = size
        self.start = start
        self.goal = goal
        self.obstacles = obstacles or []
        self.observation_space = spaces.Box(-np.inf, np.inf,
                                            shape=(9,), dtype=np.float32)
        self.action_space = spaces.Discrete(5)
        self.rewards = {'correct': 50, 'obstacle': -2, 'fail': -1}
        self.position = self.start

    def _new_trial(self, **kwargs):
        """
        new_trial() is called when a trial ends to generate the next trial.
        Here you have to set:
        The trial periods: fixation, stimulus...
        Optionally, you can set:
        The ground truth: the correct answer for the created trial.
        """
        self.position = self.start

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
            reward = self.rewards['correct']
            new_trial = True
        elif self.position in self.obstacles:
            reward = self.rewards['obstacle']
        else:
            reward = self.rewards['fail']

        return self.view, reward, False, {'new_trial': new_trial}

    @property
    def view(self):
        """
        Return the current view of the environment from the agent's perspective.
        """
        # get surrounding view
        view = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.position[0] + i < 0 or self.position[0] + i >= self.size or \
                   self.position[1] + j < 0 or self.position[1] + j >= self.size or \
                   self.position in self.obstacles:
                    view.append(-1)
                elif self.position == self.goal:
                    view.append(2)
                elif i != 0 or j != 0:
                    view.append(0)

        return np.array(view)

