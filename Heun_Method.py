# Heun method to solve differential equation dy/dx = 2y/x for y(2) using step size 0.125 and initial condition y(1) = 2

from matplotlib import pyplot as plt


def func_xy(x,y):       # Defining the function f(x,y) = dy/dx = 2y/x (slope at the point)
    val = 2*y/float(x)
    return val


def Euler(x,y):         # Predictor given by Euler method
    val = y + del_x*func_xy(x,y)
    return val


del_x = 0.125           # Number of steps
x = 1.0                 # Initial condition y(1) = 2
y = 2.0
x_new_arr = []
y_new_arr = []

while x != 2.0:
    x_new = x + del_x
    x_new_arr.append(x_new)     # x_i+1

    y_new = y + (del_x / float(2)) * (func_xy(x, y) + func_xy(x_new, Euler(x, y)))      # Corrector by Heun method
    y_new_arr.append(y_new)     # y_i+1

    print ('Value at x ={} is {}'.format(x_new, y_new))
    x = x_new           # Substituting x_i+1 value to x_i for next iteration
    y = y_new           # Substituting y_i+1 value to y_i for next Euler predictor

plt.plot(x_new_arr,y_new_arr)       # Plot the polynomial after solving the equation
plt.show()
