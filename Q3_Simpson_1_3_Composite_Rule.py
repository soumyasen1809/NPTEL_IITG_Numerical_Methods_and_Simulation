# Newton Cotes - Simpson 1/3rd Integration Rule to solve integration of sin(x) from 0 to pi/2

import numpy as np

x_0 = 0
x_n = np.pi/float(2)


def func_x(x):
    val = np.sqrt(np.abs(np.sin(x)))
    return val


num_int = 6     # Number of sub-intervals, must be even and > 2
x = np.zeros(num_int+2)
for i in range(1, len(x)):
    x[i] = x[i-1]+ ((x_n-x_0)/float(num_int+1))
print (x)

temp1 = 0
temp2 = 0
for i in range(1, num_int/2):
    temp1 = temp1 + func_x(2*x[i])
    print ('temp1 for {} is {}'.format(i, temp1))
for i in range(1, num_int/2 + 1):
    temp2 = temp2 + func_x((2*x[i])-1)
    print ('temp2 for {} is {}'.format(i, temp2))

del_x = (x_n - x_0)/float(num_int)
int_val = (del_x/float(3))*(func_x(x_0) + func_x(x_n) + 2*(temp1) + 4*(temp2))

print ('The integration value for {} sub-intervals is:  {}'.format(num_int,int_val))
