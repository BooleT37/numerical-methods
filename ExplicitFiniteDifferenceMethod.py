import math
import numpy as np

from functionutils import init_value, left_boundary_value, right_boundary_value, count_g
from utils import inclusive_range


class ExplicitFiniteDifferenceMethod:
    def __init__(self, n, m, x_max, t_max):
        self.n = n
        self.m = m
        self.x_max = x_max
        self.t_max = t_max
        self.h = x_max / n
        self.tau = t_max / m

    def count(self):
        matrix = np.zeros((self.m + 1, self.n + 1))
        # initial values
        matrix[0] = np.vectorize(init_value)(inclusive_range(0, self.x_max, self.h))

        # left boundary values
        matrix[:, 0] = np\
            .vectorize(left_boundary_value)(inclusive_range(0, self.t_max, self.tau))\
            .reshape((1, self.m + 1))

        # right boundary values
        matrix[:, self.n] = np\
            .vectorize(right_boundary_value)(inclusive_range(0, self.t_max, self.tau))\
            .reshape((1, self.m + 1))

        for j in range(1, self.m + 1):
            for i in range(1, self.n):
                matrix[j, i] = self.count_single_value(matrix, i, j)
        return matrix

    def count_single_value(self, u, i, j):
        return self.tau * ((u[j - 1, i + 1] - 2 * u[j - 1, i] + u[j - 1, i - 1]) / (self.h ** 2) +
                           count_g(i, j - 1, self.h, self.tau)) + u[j - 1, i]



