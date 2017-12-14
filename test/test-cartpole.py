import gym
env = gym.make('CartPole-v1')
for i_episode in range(200):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # print('reward : {}'.format(reward))
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break