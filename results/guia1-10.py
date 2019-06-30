from math import log
from random import random
from matplotlib import pyplot

def plot_hist(l):
    pyplot.hist(l, bins = 100)
    pyplot.show()

def acepto_rechazo():
    l = []
    c = 1.88
    while (len(l) < 10000):
        a = random()
        u = random()
        x = 30 * (a ** 2 - 2 * (a ** 3) + a ** 4)
        if (u <= x / c):
            l.append(a)
    return l

def plot_acepto_rechazo():
    plot_hist(acepto_rechazo())

plot_acepto_rechazo()