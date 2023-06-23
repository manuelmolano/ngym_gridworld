#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri June 16 15:44:59 2023

@author: molano
"""
from gym import spaces
import neurogym as ngym

class YourTask(ngym.TrialEnv):
    metadata = {}

    def __init__(self, dt=100, timing=None, extra_input_param=None):
        super().__init__(dt=dt)
       

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

        return obs, reward, done, {'new_trial': new_trial, 'gt': gt}

