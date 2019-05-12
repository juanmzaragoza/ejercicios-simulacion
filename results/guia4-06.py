import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

a = -1.5
legend = []
for i in range(18):

	series = [1]
	for t in range(30):
		series.append(a * series[t-1])

	a = a + 0.2
	legend.append("a = "+ str(a))

	plt.plot(series)


plt.ylabel('State')
plt.xlabel('Time')
plt.legend(legend, loc='upper left')
plt.show()