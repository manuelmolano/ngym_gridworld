#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri June 26 15:44:59 2023

@author: molano
"""
import numpy as np
import matplotlib.pyplot as plt


def render(task, ax=None):
        grid = np.zeros((task.size, task.size))
        grid[task.position] = 1  # agent's position marked with 1
        grid[task.goal] = 2  # goal position marked with 0.5
        for obstacle in task.obstacles:
            grid[obstacle] = -1
        # pad grid with -1
        grid = np.pad(grid, pad_width=1, mode='constant', constant_values=-1)
        if ax is None:
             _, ax = plt.subplots()
        ax.imshow(grid, vmin=-1, vmax=2, cmap='hot')
                  
def oneD_to_twoD_view(oneD, ax=None):
        view = np.zeros((3, 3))
        view[1, 1] = 1
        counter = 0
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    view[i, j] = oneD[counter]
                    counter += 1
        if ax is None:
             _, ax = plt.subplots()
        ax.imshow(view, cmap='hot', vmin=-1, vmax=2)
