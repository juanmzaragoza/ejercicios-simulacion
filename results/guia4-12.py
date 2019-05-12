import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

print("avas= ",eig([[1, -1, 0], [-1, -3, 1], [0, 1, 1]]))

legend = []
fig = plt.figure()

x = [1]
y = [0]
z = [0]

for t in range(10):
	x.append(x[t-1] - y[t-1])
	y.append(- x[t-1] - 3 * y[t-1] + z[t-1])
	z.append(y[t-1] + z[t-1])


ax = fig.gca(projection='3d')
ax.plot(x, y, z, zdir='z', label='curve in (x,y)')

ax.set_xlabel('x(t)')
ax.set_ylabel('y(t)')
ax.set_zlabel('z(t)')
plt.show()

# plt.plot(z)

# plt.ylabel('States')
# plt.xlabel('Time')
# plt.show()