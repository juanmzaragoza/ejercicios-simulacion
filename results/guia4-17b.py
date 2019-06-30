import numpy as np
import math
from scipy import stats
from random import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

legend = []
fig = plt.figure()

x = [0.1]
y = [0.1]
At = 0.1
timestamp = [0]
g = 1
L = 1

for t in range(240):
	x.append(x[t] + y[t] * At)
	y.append(y[t] + - (g/L) * math.sin(x[t]) * At)
	timestamp.append(timestamp[t] + At)


ax = fig.gca(projection='3d')
ax.plot(x, y, timestamp, zdir='z', label='curve in (x,y)')

ax.set_xlabel('theta(t)')
ax.set_ylabel('w(t)')
ax.set_zlabel('t')
plt.show()