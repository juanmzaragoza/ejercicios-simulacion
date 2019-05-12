import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

series = [1,1]
time = 30
for t in range(time):
	series.append(series[t-1] + series[t-2])

plt.plot(series)

x = [1]
y = [1]
for t in range(time):
	x.append(x[t-1] + y[t-1])
	y.append(x[t-1])

plt.plot(x)

plt.ylabel('State')
plt.xlabel('Time')
plt.show()