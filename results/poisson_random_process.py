from math import log
from random import random
from matplotlib import pyplot
from inversa_exponencial import inversa_exponencial

def generate_poisson_random_process(lam = 1, iters = 100):
	time = [0]
	for i in range(iters):
		time.append(time[i]+inversa_exponencial(random(), lam = lam))

	ocurrences = [i for i in range(len(time))]
	return (time, ocurrences)