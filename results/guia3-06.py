import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

P = np.array([[0.6, 0.4],[0.2,0.8]])
exp = 5

for i in range(10):
	print("P ** ",exp," = ")
	print(np.linalg.matrix_power(P, exp))
	exp = exp * 2