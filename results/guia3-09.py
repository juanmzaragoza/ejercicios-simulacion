import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

P = np.array([[1, 0, 0, 0],[0.5, 0.5, 0, 0],[0, 0.5, 0.5, 0],[0, 0, 0.5, 0.5]])
exp = 5

for i in range(10):
	print("P ** ",exp," = ")
	print(np.linalg.matrix_power(P, exp))
	exp = exp * 2