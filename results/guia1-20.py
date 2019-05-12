import numpy as np
from random import random
from scipy import stats

experiments_count = 100
random_vars_count = 50

freq = 0
for exc in range(experiments_count):
	l = np.zeros(6)
	for i in range(random_vars_count):
		u = random()
		if(u < 1/6):
			l[0] = l[0] + 1
		elif(u >= 1/6 and u < 2/6):
			l[1] = l[1] + 1
		elif(u >= 2/6 and u < 3/6):
			l[2] = l[2] + 1
		elif(u >= 3/6 and u < 4/6):
			l[3] = l[3] + 1
		elif(u >= 4/6 and u < 19/24):
			l[4] = l[4] + 1
		elif(u >= 19/24):
			l[5] = l[5] + 1

	(a,p) = stats.chisquare(l)

	if(1-p<0.05):
		print(exc,") Los valores corresponden a una distribu geometrica con p=",p,",alfa=0,05")
	else:
		freq = freq + 1
		print(exc,") Los valores NO corresponden a una distribu geometrica p =",p,",alfa=0,05")

print("La H0 se rechaza con una frecuencia de ",freq/experiments_count)