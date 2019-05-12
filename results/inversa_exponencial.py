from math import log
from random import random
from matplotlib import pyplot

def plot_hist(l):
    pyplot.hist(l, bins = 100)
    pyplot.show()

def inversa_exponencial(u, lam = 1):
    return (-1/lam) * log(1 - u)

def plot_hist_inversa_exponencial(iteraciones, lam = 1):
    l = [ inversa_exponencial(random()) for i in range(iteraciones)]
    plot_hist(l)

#plot_hist_inversa_exponencial(10000, 2)