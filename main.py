import math

from ExplicitFiniteDifferenceMethod import ExplicitFiniteDifferenceMethod
from functionutils import count_error
from gui import show_plot, show_errors_plot

n_start = 5
m_start = 40
x_max = math.pi
t_max = 10


def run():
    count_for_different_n()


def count_for_default_intervals():
    efd = ExplicitFiniteDifferenceMethod(n_start, m_start, x_max, t_max)
    approx_values = efd.count()
    error = count_error(approx_values, x_max, t_max)
    show_plot(approx_values, x_max, t_max, error)


def count_for_different_n():
    n_end = 55
    n_step = 5
    errors = []
    nn = range(n_start, n_end, n_step)
    for n in nn:
        approx_values = ExplicitFiniteDifferenceMethod(n, m_start, x_max, t_max).count()
        error = count_error(approx_values, x_max, t_max)
        errors.append(error)
    title = f"N = {{{n_start}, {n_start + n_step}, ..., {n_end - n_step * 2}, {n_end - n_step}}}, M = {m_start}"
    show_errors_plot(errors, nn, title=title, xlabel="N")


def count_for_different_m():
    m_end = 440
    m_step = 40
    errors = []
    mm = range(m_start, m_end, m_step)
    for m in mm:
        approx_values = ExplicitFiniteDifferenceMethod(n_start, m, x_max, t_max).count()
        error = count_error(approx_values, x_max, t_max)
        errors.append(error)
    title = f"N = {n_start}, M = {{{m_start}, {m_start + m_step}, ..., {m_end - m_step * 2}, {m_end - m_step}}}";
    show_errors_plot(errors, mm, title=title, xlabel="M")


run()
