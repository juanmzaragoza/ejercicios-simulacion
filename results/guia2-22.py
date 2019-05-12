import numpy as np
from scipy import stats
from random import random

r = stats.poisson.rvs(5, size=1000)
total = [0 for i in range(len(r))]
for exp in  range(len(r)):
	caras = 0
	for i in range(r[exp]):
		u = random()
		if(u < 1/2):
			caras = caras + 1
	total[exp] = caras

print("media teorica=2.5")
print("media experimental=",np.mean(total))