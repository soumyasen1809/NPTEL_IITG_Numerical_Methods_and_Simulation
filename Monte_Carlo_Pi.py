# Use Monte Carlo Integration to calculate the value of pi

import random

itns = 1000     # Number of iterations
count = 0       # Counter for number of points in the circle of radius 1

for i in range(0, itns):
    x_rand = random.random()        # Random X co-ordinates; random.random() gives random values from 0 to 1
    y_rand = random.random()        # Random Y co-ordinates; the max value is 1

    if x_rand**2 + y_rand**2 < 1:   # Condition for points inside the circle region x^2 + y^2 = 1
        count = count + 1

pi_val = 4*(count/float(itns))

print ('Value of pi via Monte Carlo Method is:  {}'.format(pi_val))
print ('Error is {}'.format(pi_val - (22/float(7))))
