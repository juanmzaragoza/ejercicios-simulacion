from math import log
from random import random
from matplotlib import pyplot
from poisson_random_process import generate_poisson_random_process

(x, y) = generate_poisson_random_process(1, 100)
pyplot.step(x, y, data=None, where='post')
pyplot.show()