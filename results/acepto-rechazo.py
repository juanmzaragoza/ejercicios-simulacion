from math import log
from random import random
from matplotlib import pyplot

def plot_hist(l):
    pyplot.hist(l, bins = 100)
    pyplot.show()

def acepto_rechazo():
    l = []
    y = 1
    c = 2.11
    while (len(l) < 10000):
        a = random()
        u = random()
        x = 20 * a * ((1 - a) ** 3)
        if (u <= x / c):
            l.append(a)
    return l

def plot_acepto_rechazo():
    plot_hist(acepto_rechazo())

plot_acepto_rechazo()