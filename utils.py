import numpy as np


def inclusive_range(start=None, stop=None, step=1):
    arr = np.arange(start, stop, step)
    return np.append(arr, stop)
