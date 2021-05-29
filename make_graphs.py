import matplotlib.pyplot as plt
import numpy as np
import solution as s
#Bound = 30
step = 0.01
ranged = 500
x = s.graph_p(ranged, step)[0]
y = s.graph_p(ranged, step)[1]
plt.figure(figsize=(9, 7))
plt.plot(x, np.arctan(np.sqrt(x/np.arctan(x) - 1))/np.arctan(x), label='Cauchy', color='r')
plt.plot(x, y, label='Gauss', color='g', linestyle='--')
#plt.plot(x, x/(np.arctan(x))-1, label='Cauchy', color='r')
#plt.plot(x, np.arctan(x)/np.arctan(B), label='Cauchy', color='r')
plt.title('Distribution', fontsize=15)
plt.xlabel('Boundary', fontsize=12, color='blue')
#plt.ylabel('P(x, B=' + str(B) + ')', fontsize=12, color='blue')
plt.ylabel('P(B,σ(B))', fontsize=12, color='blue')
plt.grid(True)
plt.legend()
plt.show()
