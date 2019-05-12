from math import log
from random import random
from matplotlib import pyplot

def inversa_ej_11(u):
    return 1 / (1- (4 / 5) * u)

def plot_hist(l):
    pyplot.hist(l, bins = 100)
    pyplot.show()

def plot_ej_11():
    l = [ inversa_ej_11(random()) for i in range(10000)]
    plot_hist(l)

plot_ej_11()

