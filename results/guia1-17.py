from math import *
from random import random
from matplotlib import pyplot
from common import *

def generador_bernoulli(p):
	u = random()
	return 1 if u	< p else 0

def generador_binomial(n,p):
	return sum([ generador_bernoulli(p) for i in range(n) ])

# print("n=5, p=0.5",generador_binomial(5,0.5))
# print("n=25, p=0.5",generador_binomial(25,0.5))
# print("n=50, p=0.5",generador_binomial(50,0.5))

# print("n=5, p=0.1",generador_binomial(5,0.1))
# print("n=25, p=0.1",generador_binomial(25,0.1))
# print("n=50, p=0.1",generador_binomial(50,0.1))

plot_hist([ generador_binomial(50,0.5) for i in range(1000) ])
