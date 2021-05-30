import numpy as np
from scipy import integrate


N = 10000
m_y = 100
m_x = 100
Z = []
rounded = 4
while len(Z) < N:
    y = np.random.poisson(m_y)
    x = np.random.poisson(m_x)
    while y == 0:
        y = np.random.poisson(m_y)
    Z.append(round(x/y, rounded))

M = sum(Z)/N
n = 0
dispersion = 0
while n < len(Z):
    dispersion += (Z[n] - M)**2
    n += 1
dispersion = round(dispersion/len(Z), rounded)
sigma = round(np.sqrt(dispersion), rounded)


def gauss(t, sig, m):
    z = t - m
    return np.exp(-np.power(z, 2)/(2*sig**2))*(1/(sig*np.sqrt(2*np.pi)))


def erf(sig, m, d, c):
    return integrate.quad(gauss, d, c, args=(sig, m))


def checker(a, b, z):
    i = 0
    j = 0
    while i < N:
        if a <= z[i] < b:
            j += 1
        i += 1
    return j


init_a = 0.4
end_b = 1.8
step = 0.056
p = []
p_t = []
while init_a < end_b:
    p.append(checker(init_a, init_a + step, Z)/N)
    init_a += step
init_a = 0.4
while init_a < end_b:
    p_v = erf(sigma, M, init_a, init_a + step)[0]
    p_t.append(round(p_v, rounded))
    init_a += step
print(p)
print(p_t)






