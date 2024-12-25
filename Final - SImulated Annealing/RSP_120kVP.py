import numpy as np
from scipy.optimize import minimize

def RPS(d, T, n):
    # Objective function
    def fun(x):
        return (x[4] * (((x[0] * x[1]) / ((d + x[0]) * (d + x[1]))) ** x[2]) * np.exp(-0.15002 * d) +
                         (1 - x[4]) * (0.2880 * np.exp(-0.2897 * d) + 0.5000 * np.exp(-0.2807 * d) +
                                       0.1690 * np.exp(-0.2417 * d) + 0.0430 * np.exp(-0.2342 * d)) - T) ** 2

    vfval = np.zeros(n)
    vx = np.zeros((4, n))

    # Loop
    for i in range(n):
        # Initial guess
        x0 = np.random.rand(4)
        # Solver options
        options = {'maxiter': int(1e6), 'disp': False}
        bounds = [(0, 10), (0, 10), (0, 10), (0, 10)]
        
        # Optimization
        res = minimize(fun, x0, bounds=bounds, options=options)
        x = res.x
        fval = res.fun
        
        vfval[i] = fval  # Store objective function values
        vx[:, i] = x    # Store parameter values

    Imin = np.argmin(vfval)
    fval = vfval[Imin]
    xmin = vx[:, Imin]

    return xmin, fval

