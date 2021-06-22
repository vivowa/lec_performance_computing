import numpy as np
from numpy import newaxis

def naive_mandelbrot(n, threshold):
    # A grid of c-values
    x = np.linspace(-2, 1, 5000)
    y = np.linspace(-1.5, 1.5, 5000)

    c = x[:,newaxis] + 1j * y[newaxis,:]

    z = 0

    for j in range(n):
        z = z**2 + c
    mandelbrot_set = (abs(z) < threshold)
    return mandelbrot_set


def numba_mandelbrot(n, threshold):
    # A grid of c-values
    x = np.linspace(-2, 1, 5000)
    y = np.linspace(-1.5, 1.5, 5000)

    c = x[:,newaxis] + 1j * y[newaxis,:]

    z = 0

    for j in range(n):
        z = z**2 + c
    mandelbrot_set = (abs(z) < threshold)
    return mandelbrot_set

