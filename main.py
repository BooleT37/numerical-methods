import math
import numpy as np

class ExplicitFiniteDifferenceMethod:
    def __init__(self, n, m, x_max, y_max):
        self.n = n
        self.m = m
        self.x_max = x_max
        self.y_max = y_max
        self.h = x_max / n
        self.tau = y_max / m
        self.a = - self.tau / (self.h ** 2)
        self.b = 1 - (2 * self.tau / (self.h ** 2))
        self.c = self.tau / (self.h ** 2)

    def count(self):
        matrix = np.zeros((self.m, self.n))
        initial_value = np.array(map(count_init_value, range(self.n)))
        matrix[0] = initial_value
        boundary_condition = np.array(map(count_left_boundary_value, range(self.m))).reshape((1, self.m))
        matrix[:0] = boundary_condition

        for j in range(1, self.m):
            for i in range (1, self.n):
                matrix[j, i] =

    def count_single_value(self, matrix, i, j):
        return something

    def count_d(self, i, j):
        return self.tau * (math.sin(i * self.h) + ((2 * j * self.tau) / ((j ** 2) * (self.tau ** 2) + 1)))


def count_init_value(x):
    return math.sin(x)

def count_left_boundary_value(t):
    return math.log(t ** 2 + 1, math.e)