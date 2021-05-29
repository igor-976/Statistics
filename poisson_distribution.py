import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

N = 10000
m_y = 100
m_x = 100
Z = []
while len(Z) < N:
    y = np.random.poisson(m_y)
    x = np.random.poisson(m_x)
    while y == 0:
        y = np.random.poisson(m_y)
    Z.append(round(x/y, 4))

expected_value = sum(Z)/len(Z)
dispersion = 0
n = 0
while n < len(Z):
    dispersion += (Z[n] - expected_value)**2
    n += 1
dispersion = round(dispersion/(len(Z) - 1), 3)
third_moment = 0
n = 0
while n < len(Z):
    third_moment += (Z[n] - expected_value)**3
    n += 1
third_moment = round(third_moment/(len(Z)), 3)
asymmetry = third_moment/(np.sqrt(dispersion))**3
#print('M = ', round(expected_value, 3))
#print('D = ', dispersion)
#print('M3 = ', round(third_moment, 3))
#print('A = ', round(asymmetry, 3))

#plt.figure(figsize=(8, 7))
#Y = np.random.poisson(5, 10000)
Y = np.random.normal(expected_value, np.sqrt(dispersion), 10000)
Dat = {'Gauss': Y, 'X/Y': Z}
sns.displot(data=Dat, bins=30,  stat='density')
#sns.displot(Y, bins=30,  stat='density')
#sns.kdeplot(Y, linestyle='--')
#sns.kdeplot(Z)
#plt.text(1.62, 2.7, '-- Gauss')
#plt.text(1.62, 2.55, '— X/Y')
#plt.legend()
#sns.ecdfplot(data=Z) #функция вероятности
plt.title('m_x=' + str(m_x) + '; m_y=' + str(m_y))
#sns.displot(Z, bins=30,  stat='density') #другой вид гистограммы
#sns.kdeplot(bw_adjust=0.4,  data=Y)
#plt.ylabel('Cumulative distribution function')
plt.xlabel('Z')
#plt.text(0.4, 2.7, 'M = ' + str((round(expected_value, 3))))
#plt.text(0.4, 2.55, 'σ = ' + str(round(np.sqrt(dispersion),3)))
#plt.text(1.5, 2.5, 'Third Moment = ' + str(round(third_moment, 3)))
#plt.text(1.5, 2.4, 'Asymmetry = ' + str(round(asymmetry, 3)))
#plt.savefig('pictures/ Graph')
plt.show()
#plt.hist(Z, bins=30, density=True, label='Z', color='#E69F00')
#plt.hist(Y, bins=30, density=True, label='Y', color='#56B4E9')
#plt.legend(loc='upper right')
#plt.show()


def graph(b):
    plt.xlabel('Z = X/Y')
    plt.ylabel('N = 10000')
    if b:
        plt.title('Density')
    else:
        plt.title('A bar chart')
    count, bins, ignored = plt.hist(Z, bins=30, density=b)
    plt.show()

#graph(True)
#graph(False)










