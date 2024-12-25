import numpy as np
import time

def GSA(fun, x, l=None, u=None, qv=2.7, qa=-5, Imax=400):
    """
    GSA find the optimum of a function by the Generalized Simulated Annealing Method
    Inputs: 
        fun: objective function
        x: initial guess for the optimum
        l: lower bounds for the optimum
        u: upper bounds for the optimum
        qv: visiting parameter
        qa: acceptance parameter
        Imax: maximum number of iterations
    Outputs:
        xo: solution vector
        fo: objective function value at solution vector
        time: calculation time
    """
    
    start_time = time.time()
    
    if l is None or u is None:
        l = []
        u = []
    
    xo = x
    fx = fun(x)
    fo = fx
    Dim = np.size(x)  # Size of solution vector
    
    if qv >= 3 or qv < 1:
        raise ValueError('Please enter a valid value for qv: 1 <= qv <= 3')
    elif qa < -5:
        raise ValueError('Please enter a valid value for qa: -5 <= qa <= -1')
    
    k = 1.38e-23  # Boltzmann constant (J/K)

    # External loop
    for t in range(1, Imax + 1):
        # Cooling Schedule
        Tqvo = Imax  # Initial visiting temperature
        if qv == 1.00:
            Tqv = Tqvo / np.log(1 + t)  # Classical Simulated Annealing (CSA)
        elif qv == 2.00:
            Tqv = Tqvo / (1 + t)  # Fast Simulated Annealing (FSA)
        else:
            Tqv = Tqvo * ((2**(qv - 1)) - 1) / (((1 + t)**(qv - 1)) - 1)  # Generalized Simulated Annealing (GSA)
        
        # Acceptance temperature
        Tqa = Tqv / t
        
        # Visiting Distribution of Tsallis (to be implemented)
    
    calculation_time = time.time() - start_time
    return xo, fo, calculation_time

