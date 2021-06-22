"""
Uses unittest. 

This will be our test to make sure we don not make a faster but erroneous function!

"""

import unittest
from scipy.linalg import toeplitz
import numpy as np

import project as proj

class TestPTNaive(unittest.TestCase):

    def setUp(self):
        # This will contain a list of the methods we will test
        self.methods = ['proj.naive_mandelbrot']
        
    def test_specific(self):
        X = np.array([[1.0, 2.1, 2.0], [1.8, 1.2, 1.9], [2.0, 2.2, 0.8]])
        yh = np.array([1.0, 2.0, 2.0])

        for m in self.methods:
            y = eval(m)
            self.assertTrue(np.allclose(toeplitz(y), toeplitz(yh)))


if __name__ == '__main__':
    unittest.main()
