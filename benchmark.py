"""
Code to call all our different functions and a basis for possible
profiling

"""

import numpy as np
import time
import matplotlib.pyplot as plt

import project as proj

methods = ['proj.naive_mandelbrot(25, 2)']


for m in methods:
    y = eval(m)
    tic = time.time()
    y = eval(m)
    toc = time.time() - tic

    print('{:30s} : {:10.2e} [s]'.format(m, toc))


mandelbrot_set = proj.naive_mandelbrot(25, 2)

plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5], cmap=plt.get_cmap('hot'))
plt.show()
