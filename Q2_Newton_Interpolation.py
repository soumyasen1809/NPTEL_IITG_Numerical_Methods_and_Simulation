# Newton Interpolation Method to find log(2.5) (see problem image Q2)

import numpy as np
from matplotlib import pyplot as plt

xi = np.linspace(1,4,4)
log_xi = np.zeros(4)
log_xi[1] = 0.3010
log_xi[2] = 0.4771
log_xi[3] = 0.6021


def f_x1_x2(a,b):
    val = (log_xi[b] - log_xi[a])/float(b-a)
    return val


def poly_num(a):
    val = coeff[0] + coeff[1] * (a - xi[0]) + coeff[2] * (a - xi[0]) * (a - xi[1])
    return val


coeff = np.zeros(4)
coeff[0] = log_xi[0]
coeff[1] = f_x1_x2(0, 1)
coeff[2] = (f_x1_x2(1,2) - f_x1_x2(0,1))/float(xi[2] - xi[0])
coeff[3] = (((f_x1_x2(2,3) - f_x1_x2(1,2))/float(xi[3] - xi[1])) - ((f_x1_x2(1,2) - f_x1_x2(0,1))/float(xi[2] - xi[0])))/float(xi[3] - xi[0])

print ('The coefficients are: {}, {}, {}, {}'.format(coeff[0], coeff[1], coeff[2], coeff[3]))

num = 2.5   # Value of Polynomial at 2.5 needs to be found out
poly_num_val = poly_num(num)
print ('The value of polynomial at num = {} is {}'.format(num, poly_num_val))

polynomial_arr = []
x_points = 10
for i in range(0, x_points):
    polynomial_arr.append(poly_num(i))

plt.plot(polynomial_arr)
plt.title('Polynomial plot')
plt.show()
