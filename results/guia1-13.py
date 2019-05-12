from random import random

for N in [10, 50, 100, 200, 1000]:
	xn = [ random() for i in range(N)]

	xn = list(map(lambda x: 20 * x - 5,xn))
	mean = sum(xn) / N

	v = map(lambda x: (x - mean) ** 2, xn)
	var = sum(v) / N

	print("N=",N," E(X)=",mean," V(X)=",var)
		


