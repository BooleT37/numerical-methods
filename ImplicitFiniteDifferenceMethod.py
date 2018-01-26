import numpy as np

from GridMethod import GridMethod
from TDMAsolver import tdma_solver
from functionutils import count_g


class ImplicitFiniteDifferenceMethod(GridMethod):
    def __init__(self, n, m, x_max, t_max):
        super().__init__(n, m, x_max, t_max)
        self.a = self.c = -(self.tau / (self.h ** 2))
        self.b = 1 + (2 * self.tau) / (self.h ** 2)
        self.aa = np.full(self.n - 2, self.a)
        self.bb = np.full(self.n - 1, self.b)
        self.cc = np.full(self.n - 2, self.c)

    def count(self):
        matrix = self.get_initial_matrix()

        for j in range(1, self.m + 1):
            xx = tdma_solver(self.aa, self.bb, self.cc, self.count_dd(matrix, j))
            matrix[j, 1:self.n] = xx
        return matrix

    def count_dd(self, matrix, j):
        dd = np.ndarray(shape=self.n - 1)
        dd[0] = self.count_d(matrix, 1, j) - self.a * matrix[j, 0]
        for ind in range(1, self.n - 2):
            dd[ind] = self.count_d(matrix, ind + 1, j)
        dd[self.n - 2] = self.count_d(matrix, self.n - 1, j) - self.c * matrix[j, self.n]
        return dd

    def count_d(self, matrix, i, j):
        return matrix[j - 1, i] + self.tau * count_g(i, j - 1, self.h, self.tau)
