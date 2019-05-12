from math import log
from random import random
from matplotlib import pyplot
from inversa_exponencial import inversa_exponencial

def plot_hist(l):
    pyplot.hist(l, bins = 100)
    pyplot.show()

def acepto_rechazo():
    l = []
    c = 2
    while (len(l) < 10000):
        a = inversa_exponencial(random())
        u = random()
        x = 2 - a
        if (u <= x / (c*math.exp(-a))):
            l.append(a)
    return l

def plot_acepto_rechazo():
    plot_hist(acepto_rechazo())

plot_acepto_rechazo()