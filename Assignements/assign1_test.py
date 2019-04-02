import matplotlib.pyplot as plt
import numpy as np

next_x = .5         # start value of x
next_y = -.5        # start value of x
gamma = 0.1         # step size
precision = 0.0001  # Stopping criterion
max_iters = 20      # Maximum number of iterations

# Derivative function
def df (var,x,y):
    if var == 'x':
        return (6*(1-x)*(np.exp(-x**2-y**2)) + 20*x*np.exp(-x**2-y**2)*(-x**3+x/5-y**5) + (2/3)*(x+1)*(np.exp(-(x+1)**2-y**2)) - 10*(1/5 - 3*x**2)*(np.exp(-x**2-y**2)) - 6*x*(1-x)**2*(np.exp(-x**2-(y+1)**2)))
    elif var == 'y':
        return (50*y**4*(np.exp(-x**2-y**2)) - 6*(1-x)**2*(y+1)*(np.exp(-x**2-(y+1)**2)) + 20*y*(np.exp(-x**2-y**2))*(-x**3+x/5-y**5) + 2/3*y*(np.exp(-(x+1)**2-y**2)) )
    
# for i in range(max_iters):
current_x = next_x
current_y = next_y                                                                                               
next_x = current_x - gamma * df('x',x,y)
next_y = current_y - gamma * df('y',x,y)
step = ((next_x - current_x)**2 - (next_y - current_y)**2)**0.5 


print("Minimum at", next_x,next_y)
