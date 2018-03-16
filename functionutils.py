import math

import numpy as np


def init_value(x, y):
    return math.sin(x + y)


def x_boundary_value(y, t):
    return math.sin(y) + math.log(t ** 2 + 1)


def y_boundary_value(x, t):
    return math.sin(x) + math.log(t ** 2 + 1)


def count_exact_values(n, m, x_max, t_max):
    h = x_max / n
    tau = t_max / m
    t = 0
    values = np.ndarray((m + 1, n + 1, n + 1))
    for k in range(m + 1):
        x = 0
        for i in range(n + 1):
            y = 0
            for j in range(n + 1):
                exact_value = count_exact_value(x, y, t)
                values[k, j, i] = exact_value
                y = y + h
            x = x + h
        t = t + tau
    return values


def count_exact_value(x, y, t):
    return math.sin(x + y) + math.log(t ** 2 + 1)


def count_errors_for_layers(approx_values, x_max, t_max):
    m = approx_values.shape[0] - 1
    n = approx_values.shape[1] - 1
    h = x_max / n
    tau = t_max / m

    coeff = countStabilityKoeff(h, tau)
    print(f"Stability koeff is {coeff}. " + ("method converges" if coeff <= 0.5 else "method doesn't converge"))

    errors_for_layers = np.zeros(m + 1)
    exact_values = count_exact_values(n, m, x_max, t_max)
    errors = np.zeros((m + 1, n + 1, n + 1))
    t = 0
    for k in range(m + 1):
        max_err = 0
        y = 0
        for j in range(n + 1):
            x = 0
            for i in range(n + 1):
                err = abs(approx_values[k, j, i] - exact_values[k, j, i])
                if err > max_err:
                    max_err = err
                if 0 < i < n and j > 0:
                    errors[k, j, i] = err
                x = x + h
            y = y + h
        errors_for_layers[k] = max_err
        t = t + tau

    return errors_for_layers


def count_lambda1(y, i, j, h):
    return (y[j, i + 1] - 2 * y[j, i] + y[j, i - 1]) / (h ** 2)


def count_lambda2(y, i, j, h):
    return (y[j + 1, i] - 2 * y[j, i] + y[j - 1, i]) / (h ** 2)


def countStabilityKoeff(h, tau):
    return tau * (2 / (h ** 2))
