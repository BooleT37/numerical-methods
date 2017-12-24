import math

import numpy as np


def init_value(x):
    return math.sin(x)


def left_boundary_value(t):
    return math.log(t ** 2 + 1, math.e)


def right_boundary_value(t):
    return math.log(t ** 2 + 1, math.e)


def count_exact_values(n, m, x_max, t_max):
    h = x_max / n
    tau = t_max / m
    t = 0
    values = np.ndarray((m + 1, n + 1))
    for j in range(m + 1):
        x = 0
        for i in range(n + 1):
            values[j, i] = count_exact_value(x, t)
            x = x + h
        t = t + tau
    return values


def count_exact_value(x, t):
    return math.sin(x) + math.log1p(t ** 2 + 1)


def count_error(approx_values, x_max, t_max):
    m = approx_values.shape[0] - 1
    n = approx_values.shape[1] - 1
    max_err = 0
    h = x_max / n
    tau = t_max / m

    exact_values = count_exact_values(n, m, x_max, t_max)
    t = 0
    for j in range(m + 1):
        x = 0
        for i in range(n + 1):
            err = abs(approx_values[j, i] - exact_values[j, i])
            if err > max_err:
                max_err = err
            x = x + h
        t = t + tau

    return max_err