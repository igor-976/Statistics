import numpy as np
from collections import Counter
N = 10000
m_y = 4
m_x = 2
Z = []
while len(Z) < N:
    y = np.random.poisson(m_y)
    x = np.random.poisson(m_x)
    while (y == 0) or (x == 0):
        y = np.random.poisson(m_y)
        x = np.random.poisson(m_x)
    Z.append(round(x/y, 4))


a = dict(Counter(Z))
values = list(a)
lis = []
for d in a:
    lis.append(a[d])
print(max(lis))
print(values[lis.index(max(lis))])
print(max(lis)/N)