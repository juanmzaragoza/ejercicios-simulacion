import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

# it starts working
p1 = 0.8
p2 = 1 - p1

P = np.array([[0, p1,0,0,p2],[p1,0,p2,0,0],[0,p1,0,p2,0],[0,0,p1,0,p2],[p1,0,0,p2,0]])
exp = 5

for i in range(10):
	print("P ** ",exp," = ")
	print(np.linalg.matrix_power(P, exp))
	exp = exp * 2

states = [0]
for i in range(10):
	u = random()
	if(u < p1):
		if states[i-1] == 0:
			states.append(4)
		else:
			states.append(states[i-1]-1)
	else:
		if states[i-1] == 4:
			states.append(0)
		else:
			states.append(states[i-1]+1)

plt.plot(states)
plt.ylabel('State')
plt.xlabel('Time')
plt.show()