# Nonlinear Equation to solve is: f(x) = a - 1/x = 0 for a>0 (Non linear equation)

import numpy as np
from matplotlib import pyplot as plt

a = 0.2     # Defining a = 0.2
count = 0   # Count number of iterations
x_0 = 0.01   # Initial guess value
eps = 100   # Error epsilon

err = []


while eps > 0.005:    # Tolerance value epsilon is 0.5 taken
    f_x0 = a - (1/float(x_0))
    diff_f_x0 = 1/float(x_0**2)
    x_1 = x_0 - (f_x0/float(diff_f_x0))     # Next value x_1
    x_0 = x_1       # Substituting current value of x with new value for next iteration
    eps = (1/float(a) )- x_1    # Calculate error
    count = count + 1
    err.append(eps)

print ('The iterated value is {}'.format(x_1))
print ('Error is {}'.format(eps))
print ('Number of iterations are {}'.format(count))

plt.plot(err)
plt.show()
