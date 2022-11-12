import numpy as np
import matplotlib.pyplot as plt


rs = np.linspace(1, 4, 1000)  # 1000 steps for r to go from 1 to 4
N = 500
x = np.zeros(N)
x[0] = 0.5
equi = np.arange(round(N * 0.9), N)  # index of last 10% of N

for i in range(len(rs)):
    for n in range(N - 1):
        x[n + 1] = rs[i] * x[n] * (1 - x[n])

    uniq = np.unique(x[equi])  # plotting only the unique values of x
    r = rs[i] * np.ones(
        len(uniq)
    )  # need same number of r as we have unique elements to be able to plot

    plt.plot(r, uniq, "k.", markersize=1)

plt.show()

