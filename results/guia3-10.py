import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

P = np.array([[0.2, 0.8],[0.4, 0.6]])
exp = 5

for i in range(15):
	print("P ** ",exp," = ")
	print(np.linalg.matrix_power(P, exp))
	exp = exp * 2

for i in range(10):
	worker = []
	for day in range(20):
		if(day == 0):
			u = random()
			if(u < 0.1):
				worker.append(1) # late
			else:
				worker.append(0)	# early
		else:
			u = random()
			if(worker[day-1] == 1): # arrives late
				if(u < 0.2):
					worker.append(1)
				else:
					worker.append(0)
			else: # arrives early
				if(u < 0.4):
					worker.append(1)
				else:
					worker.append(0)

	plt.plot(worker)
	plt.ylabel('State')
	plt.xlabel('Time')
	plt.show()