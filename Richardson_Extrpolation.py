# Richardson Method to solve is: f(x)=  -0.1x^4 -0.15x^3 -0.5x^2 -0.25x +1.2  |   Calculate derivative at x = 0.5

del_x1 = 0.5    # Delta x1 chosen
del_x2 = 0.1    # Delta x2 chosen


def func_x(x):  # Define the function f(x)
    val = -0.1*(x**4) -0.15*(x**3) -0.5*(x**2) -0.25*(x) +1.2
    return val


def diff_func_x(x,h):   # Define derivative of f(x) as the central difference of the function
    val = (func_x(x+h) - func_x(x-h))/float(2*h)
    return val


# Calculate the derivative of the function based on Richardson Method
val_x = diff_func_x(0.5,del_x2) + (diff_func_x(0.5, del_x2) - diff_func_x(0.5, del_x1))/float(((del_x1/float(del_x2))**2)-1)

print ('derivative of function at x = 0.5 is:   {}'.format(val_x))
