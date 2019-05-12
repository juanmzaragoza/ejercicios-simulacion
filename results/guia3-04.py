import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

# it starts working
checks = 40
states = [0]
for i in range(checks):
	u = random()
	if(states[i-1] == 1):
		if(u < 0.95): #continue working
			states.append(1)
		else:
			states.append(0)
	else:
		if(u < 0.4): # if was break
			states.append(1)
		else:
			states.append(0)

plt.plot(states)
plt.ylabel('State')
plt.xlabel('Time')
plt.show()