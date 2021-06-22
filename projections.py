"""
Methods for projection onto the set of symmetric Toeplitz matrices

"""

# No-op for use with profiling and test
try:
    @profile
    def f(x): return x
except:
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner


import numpy as np


def toeplitz_numpy(X):
    """
    Project X on the set of symmetric Toeplitz matrices. 

    Returns the first column of the result. 

    INPUT:
    X     Numpy array (n x n)
    
    OUTPUT:
    y     First column of resulting Toeplitz matrix, numpy array (n x 1)

    
    """

    n = X.shape[0]

    y = np.zeros((n, 1))

    r = 0.0 
    for i in range(n):
        r += X[i, i]
    y[0] = r/n

    for i in range(1, n):
        r = 0.0
        for j in range(n-i):
            r += X[i+j, j] + X[j, i+j]
            
        y[i] = r/(2*(n-i))

    return y



@profile
def toeplitz_numpy_vec(X):
    """
    Project X on the set of symmetric Toeplitz matrices. 

    Returns the first column of the result. 

    INPUT:
    X     Numpy array (n x n)
    
    OUTPUT:
    y     First column of resulting Toeplitz matrix, numpy array (n x 1)

    
    """

    n = X.shape[0]

    y = np.zeros((n, 1))

    r = 0.0 
    for i in range(n):
        r += X[i, i]
    y[0] = r/n

    for i in range(1, n):
        r = 0.0

        ud = np . diag (X , i ) # upper diagonal
        ld = np . diag (X , -i) # lower diagonal
        y[i ] = 0.5*( np . mean ( ud ) + np . mean ( ld ))
   
    return y

