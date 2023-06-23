#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri June 16 15:44:59 2023

@author: molano
"""
import numpy as np
from gym import spaces
import neurogym as ngym

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
        'tags': ['perceptual', 'two-alternative', 'supervised']
    }
    def __init__(self, dt=100):
        super().__init__(dt=dt)
        name = {'fixation': 0, 'stimulus': range(1, 9)}
        self.observation_space = spaces.Box(
            -np.inf, np.inf, shape=(9,), dtype=np.float32)
        self.action_space = spaces.Discrete(5)
    def new_trial(self, **kwargs):
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
        obs = 0
        reward = 0
        done = False
        new_trial = False
        gt = 0
        return obs, reward, done, {'new_trial': new_trial, 'gt': gt}


if __name__ == '__main__':
   task = YourTask(dim_ring=4)
   task.reset()
   print(task)