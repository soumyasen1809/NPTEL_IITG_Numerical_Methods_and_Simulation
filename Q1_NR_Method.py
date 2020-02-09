# Newton Raphson Equation to solve spherical tank problem (see problem image Q1) - Pitfalls of the method
# f(h) = 30 - pi*h^2*[(9-h)/3]

import numpy as np
from matplotlib import pyplot as plt

x_0 = 5     # Initial guess - Main reason for the pitfall

eps = 10    # Error, initialized with a random big number 10
count = 0   # Count number of iterations

err = []

while eps > 0.01:   # Tolerance value taken 0.01
    f_x0 = 30 - (np.pi*(x_0**2)*((9-x_0)/float(3)))
    df_x0 = np.pi*(6*x_0 - x_0**2)
    x_1 = x_0 - (f_x0/float(df_x0))     # Newton Raphson method

    eps = np.abs((x_1 - x_0)/float(x_1))    # Error between x+1 and x
    count = count + 1                   # Count number of iterations
    err.append(eps)

    x_0 = x_1       # Set old value x to new value x+1
    print (x_0)


print ('Iterative solution is:  {}'.format(x_1))
print ('Epsilon is: {}'.format(eps))
print ('Number of iterations are:   {}'.format(count))

plt.plot(err)   # Plotting how epsilon varied with iterations
plt.show()
