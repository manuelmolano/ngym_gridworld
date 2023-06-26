
from ngym_gridworld.envs import gridworld
from ngym_gridworld.usage import plotting
import matplotlib.pyplot as plt
# create a gridworld task
gw = gridworld.GridWorld(size=5, start=(0, 0), goal=(4, 4), obstacles=[(0, 2), (1, 2), (2, 2)])
max_num_tr = 10
num_tr = 0
plot_behavior = True
if plot_behavior:
    f, ax = plt.subplots(ncols=2)
while num_tr < max_num_tr:
    # step through the task
    obs, reward, done, info = gw.step(gw.action_space.sample())
    print(obs, reward, done, info)
    if info['new_trial']:
        num_tr += 1
    if plot_behavior:
        plotting.render(task=gw, ax=ax[0])
        plotting.oneD_to_twoD_view(oneD=obs, ax=ax[1])
        plt.draw()
        plt.pause(0.1)
