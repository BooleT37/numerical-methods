import math

from ExplicitFiniteDifferenceMethod import ExplicitFiniteDifferenceMethod
from functionutils import count_error
from gui import show_plot


def run(n, m, x_max, t_max):
    efd = ExplicitFiniteDifferenceMethod(n, m, x_max, t_max)
    approx_values = efd.count()
    error = count_error(approx_values, x_max, t_max)
    show_plot(approx_values, x_max, t_max, error)


run(5, 40, math.pi, 10)