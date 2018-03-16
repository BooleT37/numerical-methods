import numpy as np

from functionutils import init_value, x_boundary_value, y_boundary_value


class GridMethod:
    def __init__(self, n, m, x_max, t_max):
        self.n = n
        self.m = m
        self.x_max = x_max
        self.t_max = t_max
        self.h = x_max / n
        self.tau = t_max / m

    def get_initial_matrix(self):
        matrix = np.zeros((self.m + 1, self.n + 1, self.n + 1))
        # initial values
        y = 0
        for j in range(self.n + 1):
            x = 0
            for i in range(self.n + 1):
                matrix[0, j, i] = init_value(x, y)
                x += self.h
            y += self.h

        # x boundary values
        t = self.tau
        for k in range(1, self.m + 1):
            y = self.h
            for j in range(self.n + 1):
                matrix[k, j, 0] = matrix[k, j, self.n] = x_boundary_value(y, t)
                y += self.h
            t += self.tau

        # y boundary values
        t = self.tau
        for k in range(1, self.m + 1):
            x = self.h
            for i in range(self.n + 1):
                matrix[k, 0, i] = matrix[k, self.n, i] = y_boundary_value(x, t)
                x += self.h
            t += self.tau

        return matrix
