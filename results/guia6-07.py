from pylab import *

u = 15
A = 10
B = 1

def m1(r):
	return (1/(u - r))*( B + A*(r/u) )

def m2(r):
	return (1/((2*u) - r))*( 2*B + A*(r/(2*u) ))

l = linspace(1, 14)

plot(l, m1(l), 'r--', linewidth = 2)
plot(l, m2(l), 'b-', linewidth = 2)

plot([1], [0], 'go')

axis([0, 20, 0, 20])

xlabel('lambda')
ylabel('costo maquinas')

show()