import numpy as np
import matplotlib.pyplot as plt

N = 500
x = np.zeros(N)
x[0] = 0.4
r = 1.9

for i in range(N - 1):
    x[i + 1] = r * x[i] * (1 - x[i])
plt.plot(x, "-")
plt.show()
