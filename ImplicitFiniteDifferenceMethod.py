import numpy as np

from TDMAsolver import tdma_solver
from functionutils import count_g, init_value, left_boundary_value, right_boundary_value
from utils import inclusive_range


class ImplicitFiniteDifferenceMethod:
    def __init__(self, n, m, x_max, t_max):
        self.n = n
        self.m = m
        self.x_max = x_max
        self.t_max = t_max
        self.h = x_max / n
        self.tau = t_max / m
        self.a = self.c = -(self.tau / (self.h ** 2))
        self.b = 1 + (2 * self.tau) / (self.h ** 2)
        self.aa = np.full(self.n - 2, self.a)
        self.bb = np.full(self.n - 1, self.b)
        self.cc = np.full(self.n - 2, self.c)

    def count_dd(self, matrix, j):
        dd = np.ndarray(shape=self.n - 1)
        dd[0] = self.count_d(matrix, 1, j) - self.a * matrix[j, 0]
        for ind in range(1, self.n - 2):
            dd[ind] = self.count_d(matrix, ind + 1, j)
        dd[self.n - 2] = self.count_d(matrix, self.n - 1, j) - self.c * matrix[j, self.n]
        return dd

    def count_d(self, matrix, i, j):
        return matrix[j - 1, i] - count_g(i, j - 1, self.h, self.tau)

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
            xx = tdma_solver(self.aa, self.bb, self.cc, self.count_dd(matrix, j))
            matrix[j, 1:self.n] = xx
        return matrix