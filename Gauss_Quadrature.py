# Gauss Quadrature integration of the function e^x from -1 to 1

import numpy as np


def func_x(x):
    val = np.exp(x)
    return val


n_weights = 2
x_w = np.ones((n_weights,n_weights))
x_w[0,0] = -1/float(np.sqrt(3))
x_w[1,0] = 1/float(np.sqrt(3))

val_int = 0
for i in range(0, n_weights):
    val_int = val_int + x_w[i,1]*func_x(x_w[i,0])

print ('For {} Gauss sampling points, the integration is:   {}'.format(n_weights,val_int))
