import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt

P = np.array([[0.5, 0.5, 0, 0],[0.25, 0.75, 0, 0],[0.25, 0.25, 0.25, 0.25],[0.25, 0.25, 0.25, 0.25]])
exp = 5

for i in range(30):
	print("P ** ",exp," = ")
	print(np.linalg.matrix_power(P, exp))
	exp = exp * 2