# Bisection Method equation to solve is:    x^2 -3 in the interval [1,5]

import numpy as np
from matplotlib import pyplot as plt

x_0 = 1.0   # a - Interval opens
x_1 = 5.0   # b - Interval closes

eps = np.abs((x_1 - x_0)/float(x_1))
count = 0

err = []

while eps > 0.01:
    f_x0 = x_0**2 - 3
    f_x1 = x_1**2 - 3

    if f_x0*f_x1 < 0:
        m_0 = (x_0+x_1)/float(2)
        f_m0 = m_0**2 -3

        if f_m0*f_x0 < 0:
            x_1 = m_0
            count = count + 1
        else:
            x_0 = m_0
            count = count + 1

    eps = np.abs((x_1 - x_0) / float(x_1))
    err.append(np.sqrt(3) - m_0)

print ('Iterative value is: {}'.format(m_0))
print ('Epsilon is: {}'.format(eps))
print ('Number of iterations are:   {}'.format(count))

plt.plot(err)
plt.show()
