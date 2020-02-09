# Equation to solve by Secant Method is: f(x) = x^4 - x - 10

import numpy as np
from matplotlib import pyplot as plt

x_0 = 1.0   # Initial number 1 guess
x_1 = 3.0   # Initial number 2 guess

eps = 10    # Error between x+1 and x values
count = 0

err = []

while eps > 0.01:
    f_x0 = x_0**4 -x_0 -10
    f_x1 = x_1**4 -x_1 -10
    x_new = x_1 - (((x_1 - x_0)*f_x1)/float(f_x1 - f_x0))   # Secant method formula
    eps = np.abs(x_new - x_1)
    err.append(1.856 - x_new)       # Actual root is 1.856, so finding the error with each iterations
    x_0 = x_1       # Setting x-1 value to x
    x_1 = x_new     # Setting x value to x+1
    count = count + 1   # Increasing iteration counter

print ('Iterative solution is:  {}'.format(x_new))
print ('Epsilon is:   {}'.format(eps))
print ('Number of iterations are:   {}'.format(count))

plt.plot(err)
plt.show()
