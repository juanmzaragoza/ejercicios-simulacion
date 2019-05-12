import numpy as np
from scipy import stats
from random import random
import matplotlib.pyplot as plt
import numpy as np

r = 1
b = 1
d = 1
c = 1

K = 5

x0 = 4
y0 = 1

predador = [x0]
presa = [y0]

time = 60
legend = []

for t in range(time):#1.7976931348623157e+308
	predador.append(predador[t-1] + r * predador[t-1] * (1 - predador[t-1]/K) - d * (1 - 1 / (b * (presa[t-1] + 1))) * predador[t-1])
	presa.append(presa[t-1] - d * presa[t-1] + c * predador[t-1] * presa[t-1])

legend.append("predador")
legend.append("presa")

plt.plot(predador)
plt.plot(presa)

plt.ylabel('Population')
plt.xlabel('Time')
plt.legend(legend, loc='upper left')
plt.show()