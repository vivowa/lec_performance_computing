import os
os.environ['NUMBA_ENDABLE_CUDASIM'] = '1'

from numba import cuda
import numpy as np

host_array1 = np.arange(10)
device_array = cuda.to_device(host_array1)
device_array