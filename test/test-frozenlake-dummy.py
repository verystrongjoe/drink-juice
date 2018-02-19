import gym
import numpy as np
import random as pr
from gym.envs.registration import register

num_episodes = 2000

def rargmax(vector) :
    m = np.max(vector)
    indices = np.nonzero(vector==m)[0]
    return pr.choice(indices)

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name':'4x4','is_slippery' : False}
)
env = gym.make('FrozenLake-v3')

rList = []
Q = np.zeros([env.observation_space.n, env.action_space.n])

for i in range(num_episodes) :
    state = env.reset()
    rAll = 0
    done = False

    while not done :

        action = rargmax(Q[state, :])
        new_state, reward, done, _ = env.step(action)

        Q[state, action] = reward + np.max(Q[new_state, :])

        state = new_state
        rAll += reward

    rList.append(rAll)

print("Success rate: " + str(sum(rList) / num_episodes))
print(Q)
# plt.bar(range(len(rList)), rList, color="blue")
# plt.show()

