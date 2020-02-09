# Newton Raphson Equation to solve is: f(x) = x^2 -2 = 0

import numpy as np
from matplotlib import pyplot as plt

x_0 = 0.1     # Initial guess

eps = 10    # Error
count = 0   # Count number of iterations

err = []

while eps > 0.01:   # Tolerance value taken 0.01
    f_x0 = x_0**2 -2
    df_x0 = 2*x_0
    x_1 = x_0 - (f_x0/float(df_x0))     # Newton Raphson method

    eps = np.abs((x_1 - x_0)/float(x_1))    # Error between x+1 and x
    count = count + 1                   # Count number of iterations
    err.append(np.sqrt(2) - x_1)

    x_0 = x_1       # Set old value x to new value x+1


print ('Iterative solution is:  {}'.format(x_1))
print ('Epsilon is: {}'.format(eps))
print ('Number of iterations are:   {}'.format(count))

plt.plot(err)
plt.show()
