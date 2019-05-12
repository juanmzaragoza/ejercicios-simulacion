from math import log, sqrt
from random import random
from matplotlib import pyplot
from poisson_random_process import generate_poisson_random_process

iters = 1000
ocurrs = 0
for i in range(iters):
	(time1, ocurrences1) = generate_poisson_random_process(1, iters)
	
	if(time1[2] < 1):
		ocurrs = ocurrs + 1

print("(teo) probabilidad t2 < 1 = 0.26")
print("(exp) probabilidad t2 < 1 = ",ocurrs/iters)