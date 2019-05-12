import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 0.1
b = 0.1
c = 0.1
d = 0.1

legend = []
fig = plt.figure()

for i in range(4):

	x = [1]
	y = [1]
	time = [0]
	for t in range(30):
		x.append(a * x[t-1] + b * y[t-1])
		y.append(c * x[t-1] + d * y[t-1])
		time.append(t)

	
	a = a + 0.2
	#b = b + 0.2
	#c = c + 0.2
	d = d + 0.2
	legend.append("a = "+ str(a)+", b = "+ str(b)+", c = "+ str(c)+", d = "+ str(d))

	ax = fig.gca(projection='3d')
	ax.plot(x, y, time, zdir='z', label='curve in (x,y)')

ax.set_xlabel('x(t)')
ax.set_ylabel('y(t)')
ax.set_zlabel('t')
plt.legend(legend, loc='upper left')
plt.show()