import math
from enum import Enum

from CrankNicolsonMethod import CrankNicolsonMethod
from ExplicitFiniteDifferenceMethod import ExplicitFiniteDifferenceMethod
from ImplicitFiniteDifferenceMethod import ImplicitFiniteDifferenceMethod
from functionutils import count_error
from gui import show_plot, show_errors_plot

n_start = 5
m_start = 40
x_max = math.pi
t_max = 10


class Method(Enum):
    ExplicitFiniteDifference = 1
    ImplicitFiniteDifference = 2
    CrankNicolson = 3


METHOD_TITLES = {
    Method.ExplicitFiniteDifference: "Explicit Finite Difference method",
    Method.ImplicitFiniteDifference: "Implicit Finite Difference method",
    Method.CrankNicolson: "Crank-Nicolson method"
}


def run():
    # count_for_default_intervals(Method.CrankNicolson)
    count_for_different_n(Method.ImplicitFiniteDifference, 40, 1)
    count_for_different_m(Method.ImplicitFiniteDifference, 450, 10)


def count_for_default_intervals(method):
    if method == Method.ExplicitFiniteDifference:
        method_impl = ExplicitFiniteDifferenceMethod(n_start, m_start, x_max, t_max)
    elif method == Method.ImplicitFiniteDifference:
        method_impl = ImplicitFiniteDifferenceMethod(n_start, m_start, x_max, t_max)
    else:
        method_impl = CrankNicolsonMethod(n_start, m_start, x_max, t_max)
    approx_values = method_impl.count()
    error = count_error(approx_values, x_max, t_max)
    show_plot(approx_values, x_max, t_max, error)


def count_for_different_n(method, n_end, n_step):
    errors = []
    nn = range(n_start, n_end, n_step)
    for n in nn:
        if method == Method.ExplicitFiniteDifference:
            approx_values = ExplicitFiniteDifferenceMethod(n, m_start, x_max, t_max).count()
        elif method == Method.ImplicitFiniteDifference:
            approx_values = ImplicitFiniteDifferenceMethod(n, m_start, x_max, t_max).count()
        else:
            approx_values = CrankNicolsonMethod(n, m_start, x_max, t_max).count()
        error = count_error(approx_values, x_max, t_max)
        errors.append(error)
    title = METHOD_TITLES[method]
    title += f"\nN = {{{n_start}, {n_start + n_step}, ..., {n_end - n_step * 2}, {n_end - n_step}}}, M = {m_start}"
    title += f"\nerror(n = {n_end - n_step}) = {errors[len(errors) - 1]}"
    show_errors_plot(errors, nn, title=title, xlabel="N")


def count_for_different_m(method, m_end, m_step):
    errors = []
    mm = range(m_start, m_end, m_step)
    for m in mm:
        if method == Method.ExplicitFiniteDifference:
            approx_values = ExplicitFiniteDifferenceMethod(n_start, m, x_max, t_max).count()
        elif method == Method.ImplicitFiniteDifference:
            approx_values = ImplicitFiniteDifferenceMethod(n_start, m, x_max, t_max).count()
        else:
            approx_values = CrankNicolsonMethod(n_start, m, x_max, t_max).count()
        error = count_error(approx_values, x_max, t_max)
        errors.append(error)
    title = METHOD_TITLES[method]
    title += f"\nN = {n_start}, M = {{{m_start}, {m_start + m_step}, ..., {m_end - m_step * 2}, {m_end - m_step}}}"
    title += f"\nerror(m = {m_end - m_step}) = {errors[len(errors) - 1]}"
    show_errors_plot(errors, mm, title=title, xlabel="M")


run()
