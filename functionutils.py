import math

import numpy as np


def init_value(x):
    return math.sin(x)


def left_boundary_value(t):
    return math.log(t ** 2 + 1)


def right_boundary_value(t):
    return math.log(t ** 2 + 1)


def count_exact_values(n, m, x_max, t_max):
    h = x_max / n
    tau = t_max / m
    t = 0
    values = np.ndarray((m + 1, n + 1))
    errors = np.zeros((m + 1, n + 1))
    for j in range(m + 1):
        x = 0
        for i in range(n + 1):
            exact_value = count_exact_value(x, t)
            # print(f'({i}, {j}) -> {exact_value}')
            values[j, i] = exact_value
            if 0 < i < n and j > 0:
                error = count_error_in_point(values, i, j - 1, h, tau)
                errors[j, i] = error
            x = x + h
        t = t + tau
    return values


def count_exact_value(x, t):
    return math.sin(x) + math.log(t ** 2 + 1)


def count_error(approx_values, x_max, t_max):
    m = approx_values.shape[0] - 1
    n = approx_values.shape[1] - 1
    max_err = 0
    h = x_max / n
    tau = t_max / m

    exact_values = count_exact_values(n, m, x_max, t_max)
    errors = np.zeros((m + 1, n + 1))
    t = 0
    for j in range(m + 1):
        x = 0
        for i in range(n + 1):
            err = abs(approx_values[j, i] - exact_values[j, i])
            if err > max_err:
                max_err = err
            if 0 < i < n and j > 0:
                errors[j, i] = err
            x = x + h
        t = t + tau

    return max_err


def count_error_in_point(u, i, j, h, tau):
    return abs(u[j + 1, i] - tau * (u[j, i + 1] - 2 * u[j, i] - u[j, i - 1]) / h ** 2 + count_g(i, j, h, tau) + u[j, i])


def count_g(i, j, h, tau):
    x = h * i
    t = j * tau
    return math.sin(x) + (2 * t) / (t ** 2 + 1)