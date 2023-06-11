# FrozenLake
FrozenLake Game v1
Reinforcement Learning

Frozen Lake Environment
Frozen Lake is a simple tile-based environment in which the Al must move from an initial tile to a goal.
Tiles can be a frozen lake or a hole that keeps you stuck indefinitely.
The Al, or agent, can take four different actions: LEFT, RIGHT, UP, or DOWN. To reach the goal in the fewest number of actions, the agent must learn to avoid holes.

The game or task at hand is encapsulated by the environment. It will perform an action and then return to an object. This object contains information about the current state of the game, the reward, the discount, and whether it is a beginning, middle, or end step. The agent will operate in the environment, observe the state, and take action in accordance with its policy. It has an internal state which is trained using reinforcement learning.

My project:
 Frozen Lake game is based on reinforcement learning, and I wanted to optimize it using the Q-learning method. As you know, the agent should find its way to the goal as quickly as possible, so I implemented this optimization in the Q-table. I used three methods to achieve this, the first of which was epsilon. Epsilon causes the agent to try random paths at first, but after a while, it realizes that it should be interested in a specific approach. It goes back to doing the same thing it did successfully in the past and stops doing things that deteriorate its performance. This helps the agent understand what it needs to do, and through the scores we assigned to it, it understands which actions are good and should be taken and which are bad."
The second step was to determine the value of gamma. Gamma should be set in a way that tells the agent not to fall into the frozen lakes, the result is the agent will reach the goal faster. Another thing we need to do is to assign appropriate rewards and punishments to the agent. For example, if the agent reaches the goal, it gets a higher reward, and if it falls, it gets a negative reward. This helps the agent perform actions with more precision and not try to fall due to negative scores.

In general, we want the agent to have higher accuracy and speed by combining these three methods. The reason we have a maximum of 20 steps is that in each episode, the agent can perform 20 moves. We set the total number of episodes to 100, it means the agent can move through a total of 100 episodes. While the agent runs the episodes, the Q-table gradually completes. It is up to us how many times the agent should repeat the episodes until the Q-table becomes strong enough to solve the task. This can be done empirically. Finally, we can see the game in visual mode using the render mode.
Ps: other descriptions are available in my code.

