import gym
# import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from gym.envs.registration import register
import random as pr

def rargmax(vector) :
    m = np.max(vector)
    indices = np.nonzero(vector==m)[0]
    return pr.choice(indices)

register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4','is_slippery' : False }
)
env = gym.make('FrozenLake-v3')

Q = np.zeros([env.observation_space.n, env.action_space.n])

dis =  0.99
num_episodes = 2000

rList = []
done = False

# range(2000) ===> [1,2,3,4,5,........2000]
for i in range(num_episodes) :
    state = env.reset()
    rAll = 0
    done = False


    # episode start!!!!!
    while not done :
        # action = rargmax(Q[state, :])
        action = np.argmax(Q[state,  :] + np.random.randn(1, env.action_space.n) / (i//100+1))

        # take action
        next_state, reward, done, info = env.step(action)

        # update to train Q function
        Q[state, action] = reward + dis * np.max(Q[next_state, :])

        rAll += reward
        state = next_state

    rList.append(rAll)
    # episode close!!!

print("Succces rate : " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print(Q)
plt.bar(range(len(rList)), rList, color='blue')
plt.show()