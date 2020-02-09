# Newton Cotes Method - Trapezoidal Rule - Integration:   exp(x) dx in [-1,1]

import numpy as np
from matplotlib import pyplot as plt


def func_x(x):
    val = np.exp(x)
    return val


a = -1.0        # Lower limit of integration
b = 1.0         # Upper limit of integration
n_traps = 4     # Number of trapezoids to consider
del_x = (b-a)/float(n_traps)

temp = 0
for i in range(1,n_traps):
    temp = temp + func_x(a+i*del_x)

int_val = del_x*(func_x(a)+func_x(b))/float(2) + del_x*(temp)

print ('The integration is: {} with {} number of trapezoids'.format(int_val, n_traps))


n_traps_arr = 10
int_val_arr = []

for it in range(2, 10):
    del_x = (b-a)/float(it)
    temp2 = 0
    for i in range(1, it):
        temp2 = temp2 + func_x(a+i*del_x)

    int_val_arr.append(del_x*(func_x(a)+func_x(b))/float(2) + del_x*(temp2))

print ('The value of integration for {} trapezoids is {}'.format(it, int_val_arr[-1]))

plt.plot(int_val_arr)
plt.title('Value of area with number of trapezoids')
plt.show()
