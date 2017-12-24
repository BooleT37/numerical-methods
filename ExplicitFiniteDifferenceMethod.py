import math
import numpy as np

from functionutils import init_value, left_boundary_value, right_boundary_value


class ExplicitFiniteDifferenceMethod:
    def __init__(self, n, m, x_max, t_max):
        self.n = n
        self.m = m
        self.x_max = x_max
        self.t_max = t_max
        self.h = x_max / n
        self.tau = t_max / m
        self.a = - self.tau / (self.h ** 2)
        self.b = 1 - (2 * self.tau / (self.h ** 2))
        self.c = self.tau / (self.h ** 2)

    def count(self):
        matrix = np.zeros((self.m + 1, self.n + 1))
        initial_value = np.array(list(map(init_value, range(self.n + 1))))
        matrix[0] = initial_value
        left_boundary_values = np.array(list(map(left_boundary_value, range(self.m + 1)))).reshape((1, self.m + 1))
        matrix[:, 0] = left_boundary_values
        right_boundary_values = np.array(list(map(right_boundary_value, range(self.m + 1)))).reshape((1, self.m + 1))
        matrix[:, self.n] = right_boundary_values

        for j in range(1, self.m):
            for i in range(1, self.n):
                matrix[j, i] = self.count_single_value(matrix, i, j)
        return matrix

    def count_single_value(self, matrix, i, j):
        return self.a * matrix[j - 1, i - 1] \
               + self.b * matrix[j - 1, i] \
               + self.c * matrix[j - 1, i + 1] \
               + self.count_d(i, j - 1, )

    def count_d(self, i, j):
        return self.tau * (math.sin(i * self.h) + ((2 * j * self.tau) / ((j ** 2) * (self.tau ** 2) + 1)))

