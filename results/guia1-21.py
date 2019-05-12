import numpy as np
from random import random
from scipy import stats

muestras_a = 100
variables_a = 10

muestras_b = 100
variables_b = 20

def generador(vars_count):
	return sum([random() for i in range(vars_count)])

X_a = [ generador(variables_a) for i in range(muestras_a) ]
X_b = [ generador(variables_b) for i in range(muestras_b) ]

print(X_b)