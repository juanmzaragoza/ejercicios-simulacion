from math import log, sqrt
from random import random
from matplotlib import pyplot
from poisson_random_process import generate_poisson_random_process

iters = 100
for i in range(6):
	(time1, ocurrences1) = generate_poisson_random_process(2, iters)
	(time2, ocurrences2) = generate_poisson_random_process(5, iters)
	
	print("")
	print("lam=2, iters=",iters,", tasa de eventos=",ocurrences1[-1]/time1[-1],", error=",sqrt((ocurrences1[-1]/time1[-1]-2) ** 2))
	print("lam=5, iters=",iters,", tasa de eventos=",ocurrences2[-1]/time2[-1],", error=",sqrt((ocurrences2[-1]/time2[-1]-5) ** 2))
	print("")

	iters = iters * 10
