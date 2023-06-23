#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from gym import Wrapper
from gym import spaces


class YourWrapper(Wrapper):
    metadata = {
        'description': '',
        'paper_link': None,
        'paper_name': None,
    }

    def __init__(self, env):
        """
        Redefine main variables of the task 
	For instance, modify action or stimulus spaces by adding dimensions to them
        """
        super().__init__(env)
    
    def reset(self, step_fn=None):
        if step_fn is None:
            step_fn = self.step
        return self.env.reset(step_fn=step_fn)

    def new_trial(self, **kwargs):
        # change rep. prob. every self.block_dur trials
        if self.task.num_tr % self.block_dur == 0:
            curr_block = self.curr_block
            while curr_block == self.curr_block:
                curr_block = self.task.rng.choice(range(self.n_block))
            self.curr_block = curr_block
        probs = self.choice_prob[self.curr_block]
        kwargs = dict()
        kwargs['ground_truth'] = self.task.rng.choice(self.choices,
                                                      p=probs)
        return self.env.new_trial(**kwargs)

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        # MODIFY ANY OF THE STEP OUTPUTS (obs, reward, done, info)
        return obs, reward, done, info
