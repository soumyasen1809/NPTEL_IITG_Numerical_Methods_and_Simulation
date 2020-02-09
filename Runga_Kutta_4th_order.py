# 4th order Runga Kutta method: solve f(x,y) = 4e^0.8x -0.5y using del_x = 0.5 and initial condition y(0) = 2 in [0,0.5]

import numpy as np


def func_xy(x,y):
    val = 4*np.exp(0.8*x) -0.5*y
    return val


x_0 = 0
y_0 = 2
n_it = 4
m = np.zeros(n_it)
m[0] = func_xy(x_0,y_0)
x_new = 0.5/float(2)

for i in range(0,n_it-2):
    y_new = y_0 + m[i] * x_new
    m[i+1] = func_xy(x_new, y_new)

x_new = 0.5
y_new = y_0 + m[2]*x_new
m[3] = func_xy(x_new,y_new)
y_new = y_0 + m[3]*x_new
weighted_m = (1/float(6))*(m[0] + 2*m[1] + 2*m[2] + m[3])
y_new = y_0 + weighted_m*x_new
print ('Value of equation at x = 0.5 is {}'.format(y_new))
