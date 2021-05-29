import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def gif(m):
    n = 10000
    z = []
    while len(z) < n:
        y = np.random.poisson(m)
        x = np.random.poisson(m)
        while y == 0:
            y = np.random.poisson(m)
        z.append(round(x/y, 4))
    return z


i = 1
x = []
while i <= 30:
    values = gif(i)
    sns.kdeplot(data=values, bw_adjust=0.7)
    plt.savefig('pictures/ Graph' + str(i))
    plt.close()
    i += 1


