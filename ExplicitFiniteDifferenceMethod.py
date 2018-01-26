from GridMethod import GridMethod
from functionutils import count_g


class ExplicitFiniteDifferenceMethod(GridMethod):
    def __init__(self, n, m, x_max, t_max):
        super().__init__(n, m, x_max, t_max)

    def count(self):
        matrix = self.get_initial_matrix()

        for j in range(1, self.m + 1):
            for i in range(1, self.n):
                matrix[j, i] = self.count_single_value(matrix, i, j)
        return matrix

    def count_single_value(self, u, i, j):
        return self.tau * ((u[j - 1, i + 1] - 2 * u[j - 1, i] + u[j - 1, i - 1]) / (self.h ** 2) +
                           count_g(i, j - 1, self.h, self.tau)) + u[j - 1, i]



