from math import *
from random import random
from matplotlib import pyplot

def generacion_gaussiana():
	while(1):
		u1 = random()
		u2 = random()

		x1 = -log(u1)
		if( u2 <= exp(-((x1 - 1) ** 2)/2)):
			return x1

def generar_signo():
	if(random() >= 0.5):
		return -1
	else:
		return 1

def plot_hist(l):
    pyplot.hist(l, bins = 100)
    pyplot.show()

l = [ generacion_gaussiana() for i in range(10000)]
plot_hist(l)

l = [ generar_signo() * generacion_gaussiana() for i in range(10000)]
plot_hist(l)