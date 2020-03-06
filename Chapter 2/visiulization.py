import matplotlib.pyplot as plt
import numpy as np

R=np.load("Average Reward.npy")
A=np.load("Optimal Action.npy")
print(R.shape)
print(A.shape)

plt.plot(R[1])
plt.show()