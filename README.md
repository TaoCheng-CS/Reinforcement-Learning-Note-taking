# Notes of reinforcement learning
## Adaptive computation and machine learning.
All contents are based on the Book "*Reinforcement Learning an introduction second edition*" written by Richard S. Sutton and Andrew G. Barto. 

## Preface
As the author said 
> we retain a focus on core, online learning algorithms.

The structure of the book is showed below
1. Chapter2-8 treats as much of reinforcement learning as possible without going beyond the tabular case for which exact solutions can be found.
2. Chapter9-13 is devoted to extending the ideas to function approximation.
3. The third part of the book has large new chapters on reinforcement learning’s relationships to psychology
(Chapter 14) and neuroscience (Chapter 15), as well as an updated case-studies chapter including Atari game playing, Watson’s wagering strategy, and the Go playing programs AlphaGo and AlphaGo Zero (Chapter 16).

I think the story of Harry, Sutton and Barto is quiet motivating.

##  Chapter 1
Reinforcement learning is much more focused on gold-directed learning from interaction than other approaches to machine learning.
### Reinforcement learning
trial-and-error search and delayed reward are the two most important distinguishing features of reinforcement learning. Reinforcement learning is the third paradigm of machine learning compared with supervised and unsupervised learning. One of the challenges that arise in reinforcement learning, and not in other kinds of learning, is the trade-o↵ between exploration and exploitation. Another key feature of reinforcement learning is that it explicitly considers the whole problem of a goal-directed agent interacting with an uncertain environment. Reinforcement learning takes the opposite tack, starting with a complete, interactive, goal-seeking agent. 
The author writes:
> One must look beyond the most obvious examples of agents and their environments to appreciate the generality of the reinforcement learning framework.

### Elements of Reinforcement Learing
1. policy. A policy defines the learning agent’s way of behaving at a given time. 
2. reward. A reward signal defines the goal of a reinforcement learning problem. reward v.s. value. Whereas the reward signal indicates what is good in an immediate sense, a value function specifies what is good in the long run
3. value function. 
4. model(optionally) This is something that mimics the behavior of the environment, or more generally, that allows inferences to be made about how the environment will behave. model-based methods v.s. model-free methods. Modern reinforcement learning spans the spectrum from low-level, trial-and-error learning to high-level, deliberative planning.

### Limitations and scope
In this book, state representation is not taken into consideration.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/1.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/1.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/1.0/">Creative Commons Attribution-NonCommercial-ShareAlike 1.0 Generic License</a>.