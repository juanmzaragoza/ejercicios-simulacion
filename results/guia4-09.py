import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt
import numpy as np

a = [ 0.0005, 0.001]
K = [ 1, 0.001]
initial = 1
time = 10
legend = []

for ai in a:
	for Ki in K:
		series = [initial]

		for t in range(time):#1.7976931348623157e+308
			result = (- ((ai - 1) * series[t-1]/Ki) + ai) * series[t-1]
			if(result >= np.finfo(np.double).max):
				series.append(np.finfo(np.double).max)
			elif(result <= np.finfo(np.double).min):
				series.append(np.finfo(np.double).min)
			else:
				series.append(result)
		print(series[t])
		legend.append("a = "+ str(ai)+", K = "+ str(Ki)+", x0 = "+ str(initial))
		plt.plot(series)

plt.ylabel('Population')
plt.xlabel('Time')
plt.legend(legend, loc='upper left')
plt.show()