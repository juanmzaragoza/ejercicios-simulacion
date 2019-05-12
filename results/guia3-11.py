import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

P = np.array([[1, 0, 0, 0],[0.5, 0.5, 0, 0],[0.1, 0.3, 0.6, 0],[0.4, 0.3, 0.6, 0.1]])
init = np.array([0, 0, 0, 1])

exp = 1

while True:
	print(exp," days")
	result = np.dot(init, np.linalg.matrix_power(P, exp))
	if(result[0] > 0.8):
		break
	else:
		exp = exp + 1
		print("result:",result)

print("result:",result)
print("Total day elapsed ",exp - 1)