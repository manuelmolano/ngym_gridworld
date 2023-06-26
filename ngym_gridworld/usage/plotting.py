#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri June 26 15:44:59 2023

@author: molano
"""
import numpy as np
import matplotlib.pyplot as plt


def render(render_flag, size, position, goal, obstacles):
        if not render_flag:
            return
        grid = np.zeros((size, size))
        grid[position] = 1  # agent's position marked with 1
        grid[goal] = 0.5  # goal position marked with 0.5
        for obstacle in obstacles:
            grid[obstacle] = -1
        plt.figure(figsize=(5,5))
        plt.imshow(grid, cmap='Pastel1')
        plt.show()

def oneD_to_twoD(oneD):
        view = np.zeros((3, 3))
        counter = 0
        for i in range(0, 3):
            for j in range(0, 3):
                view[i, j] = oneD[counter]
                counter += 1