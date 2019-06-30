from pylab import *

def xeq1(r):
	return [0 for i in range(len(r))]

def xeq2(r):
	return (r - 1)/r

domain = linspace(1, 10)
domain1 = linspace(0, 1)

plot(domain1, xeq1(domain1), 'r--', linewidth = 2)
plot(domain1, xeq2(domain1), 'b-', linewidth = 2)

plot(domain, xeq1(domain), 'b-', linewidth = 2)
plot(domain, xeq2(domain), 'r--', linewidth = 2)

plot([1], [0], 'go')

axis([0, 10, -5, 5])

xlabel('r')
ylabel('x_eq')

show()