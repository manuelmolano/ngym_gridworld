
from ngym_gridworld.envs import gridworld
from ngym_gridworld.usage import plotting
import matplotlib.pyplot as plt

gw = gridworld.GridWorld()
print(gw)
max_num_tr = 10
num_tr = 0
while num_tr < max_num_tr:
    # step through the task
    obs, reward, done, info = gw.step(gw.action_space.sample())
    print(obs, reward, done, info)
    f, ax = plt.subplots(ncols=2)
    plotting.render(task=gw, ax=ax[0])
    plotting.oneD_to_twoD_view(oneD=obs, ax=ax[1])
    plt.show()
    if info['new_trial']:
        num_tr += 1
        print('new trial')