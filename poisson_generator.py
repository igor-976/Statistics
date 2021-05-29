import math as m
import random

a = 2


def p(k):
    f = (m.pow(a, k)/m.factorial(k))*m.exp(-a)
    return f


P = []
i = 0
while len(P) < 12:
    P.append(round(p(i), 5))
    i += 1

i = 1
P_new = []
while len(P_new) < 12:
    P_new.append(round(sum((P[0:i])), 5))
    i += 1


def generator():
    j = 0
    x = round(random.random(), 5)
    while x > P_new[j]:
        j += 1
    else:
        return j


Values = []
n = 0
while n < 3000:
    Values.append(generator())
    n += 1
n = 0
expected_value = sum(Values)/len(Values)
dispersion = 0
while n < len(Values):
    dispersion += (Values[n] - expected_value)**2
    n += 1
dispersion = round(dispersion/(len(Values) - 1), 3)



#print('D =', dispersion)
#print('M =', round(expected_value,3))
print(Values)
