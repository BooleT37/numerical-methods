import numpy as np

from GridMethod import GridMethod
from TDMAsolver import tdma_solver
from functionutils import count_lambda2, count_lambda1


class AlternatingDirectionMethod(GridMethod):
    def __init__(self, n, m, x_max, t_max):
        super().__init__(n, m, x_max, t_max)
        self.gamma = self.tau / (self.h ** 2)

    def count(self):
        y = self.get_initial_matrix()
        y_ext = self.extend_y(y)
        aa = cc = np.full(self.n - 2, self.gamma / 2)
        bb = np.full(self.n - 1, self.gamma - 1)

        for k in range(1, self.m * 2 + 1):
            if k % 2 == 1:
                for j in range(1, self.n):
                    y_ext[k, j, 1:self.n] = tdma_solver(aa, bb, cc, self.count_dd_i(y_ext, j, k))
            else:
                for i in range(1, self.n):
                    y_ext[k, 1:self.n, i] = np.transpose(tdma_solver(aa, bb, cc, self.count_dd_j(y_ext, i, k)))
        return y_ext[::2, :, :]

    def count_dd_i(self, y_ext, j, k):
        dd = np.ndarray(shape=self.n - 1)
        dd[0] = - self.count_f(y_ext, 1, j, k) - (self.gamma / 2) * y_ext[k, j, 0]
        for ind in range(1, self.n - 2):
            dd[ind] = - self.count_f(y_ext, ind + 1, j, k)
        dd[self.n - 2] = - self.count_f(y_ext, self.n - 1, j, k) - (self.gamma / 2) * y_ext[k, j, self.n]
        return dd

    def count_dd_j(self, y_ext, i, k):
        dd = np.ndarray(shape=self.n - 1)
        dd[0] = - self.count_phi(y_ext, i, 1, k) - (self.gamma / 2) * y_ext[k, 0, i]
        for ind in range(1, self.n - 2):
            dd[ind] = - self.count_phi(y_ext, i, ind + 1, k)
        dd[self.n - 2] = - self.count_phi(y_ext, i, self.n - 1, k) - (self.gamma / 2) * y_ext[k, self.n, i]
        return dd

    def count_f(self, y_ext, i, j, k):
        return y_ext[k, j, i] + (self.tau / 2) * count_lambda2(y_ext[k], i, j, self.h)

    def count_phi(self, y_ext, i, j, k):
        return y_ext[k, j, i] + (self.tau / 2) * count_lambda1(y_ext[k], i, j, self.h)

    def extend_y(self, y):
        y_ext = np.zeros(((self.m + 1) * 2, self.n + 1, self.n + 1))
        for k in range(self.m + 1):
            for j in range(self.n + 1):
                for i in range(self.n + 1):
                    y_ext[k * 2, j, i] = y[k, j, i]

        for k in range(self.m):
            for j in range(self.n):
                y_ext[k * 2 + 1, j, 0] = \
                    (y[k + 1, j, 0] + y[k, j, 0]) / 2 - \
                    (self.tau / 4) * (count_lambda2(y[k + 1], 0, j, self.h) - count_lambda2(y[k], 0, j, self.h))
                y_ext[k * 2 + 1, j, self.n] = \
                    (y[k + 1, j, self.n] + y[k, j, self.n]) / 2 - \
                    (self.tau / 4) * (count_lambda2(y[k + 1], self.n, j, self.h) - count_lambda2(y[k], self.n, j, self.h))
        return y_ext
