import numpy as np

from functionutils import init_value, left_boundary_value, right_boundary_value
from utils import inclusive_range


class GridMethod:
    def __init__(self, n, m, x_max, t_max):
        self.n = n
        self.m = m
        self.x_max = x_max
        self.t_max = t_max
        self.h = x_max / n
        self.tau = t_max / m

    def get_initial_matrix(self):
        matrix = np.zeros((self.m + 1, self.n + 1))
        # initial values
        matrix[0] = np.vectorize(init_value)(inclusive_range(0, self.x_max, self.h))

        # left boundary values
        matrix[:, 0] = np \
            .vectorize(left_boundary_value)(inclusive_range(0, self.t_max, self.tau)) \
            .reshape((1, self.m + 1))

        # right boundary values
        matrix[:, self.n] = np \
            .vectorize(right_boundary_value)(inclusive_range(0, self.t_max, self.tau)) \
            .reshape((1, self.m + 1))

        return matrix
