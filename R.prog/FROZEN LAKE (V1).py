import gym
import random
import numpy as np
import pygame
import time

#frozenlake environment
env=gym.make('FrozenLake-v1',desc=None,map_name="4x4", is_slippery=False,render_mode='ansi')
action_size = env.action_space.n # 4 actin in this game
state_size = env.observation_space.n #16 states



# Q table
qtable = np.zeros((state_size, action_size))
print("Init Qtable:\n")
print(qtable)


# set some numbers (related to training)
total_episodes = 100      #maximum number in each episode 
max_steps = 20            #maximum step in each episode
gamma = 0.7               #discount rate
epsilon = 0.1             #exploration rate



#                      ****GAME IS ON NOW****
print('training...')
for episode in range(total_episodes):
    #reset environment for new episode and get the initial state
    state = env.reset()[0]
    step = 0
    done = False
    # total rewards are in the episode
    total_rewards = 0
    print("EPISODE:  ",episode)
    #run the episode
    for step in range(max_steps):
        #choose an action (with epsilon-greedy)
        if random.uniform(0, 1)<epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(qtable[state,:])
    
        env.render()
        new_state, reward, done, truncated, info = env.step(action)
        
        #update Q table
        if done and reward == 0:
            reward = -5
        if new_state == state:
            reward = -1

        print("NEW STATE:", new_state, "REWARD:", reward)
        qtable[state, action] = (1 - gamma) * qtable[state, action] + gamma * (reward + np.max(qtable[new_state, :]))
        total_rewards += reward
        print("QTABLE AT", state, qtable[state])
        
        #move to the new state and check if the episode is complete
        state = new_state
        if done:
            print("Total reward:", total_rewards)
            print("GAME OVER.\n\n")
            break
        
#learned Q table
print("new Qtable")
print(qtable)

#reset the environment
env.reset()
env.close()
print("Training done. Result is going on...")



#visual environment(human instead of ansi)
env = gym.make('FrozenLake-v1',desc=None,map_name="4x4", is_slippery=False,render_mode='human')     
state = env.reset()[0]
step = 0
done = False
print('**************************')

for step in range(max_steps):
    env.render()
    if random.uniform(0, 1) < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(qtable[state, :])
    
        new_state, reward, done, truncated, info = env.step(action)
    if done:
        break
        
    state=new_state
    time.sleep(0.01)        
    
env.reset()
env.close()