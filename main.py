import math
from enum import Enum

from CrankNicolsonMethod import CrankNicolsonMethod
from ExplicitFiniteDifferenceMethod import ExplicitFiniteDifferenceMethod
from ImplicitFiniteDifferenceMethod import ImplicitFiniteDifferenceMethod
from functionutils import count_error
from gui import show_plot, show_errors_plot

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
    while True:
        method = prompt_method_number()
        prompt_method_params(method)
        print("\n\n")


def prompt_method_number():
    awaiting = True
    while awaiting:
        for i_method in [1, 2, 3]:
            print(f"[{i_method}] for {METHOD_TITLES[Method(i_method)]}")
        method = input_number_or_default("Input method number", 1)
        try:
            method = Method(int(method))
            awaiting = False
            return method
        except ValueError:
            print("Error: Not a valid number\n")


def prompt_method_params(method):
    awaiting = True
    while awaiting:
        print("[1] for 3D graph u(x, t)\n"
              "[2] for error(n)\n"
              "[3] for error(m)\n")
        graph_type = input_number_or_default("Input graph type", 1)
        if graph_type == 1:
            n = input_number_or_default("Input n", 5)
            m = input_number_or_default("Input m", 40)
            count_for_default_intervals(method, n, m)
            awaiting = False
        elif graph_type == 2:
            n_start = input_number_or_default("Input starting n", 5)
            n_end = input_number_or_default("Input final n", 50)
            n_step = input_number_or_default("Input step", 5)
            m = input_number_or_default("Input m", 40)
            count_for_different_n(method, n_start, n_end, n_step, m)
            awaiting = False
        elif graph_type == 3:
            n = input_number_or_default("Input n", 5)
            m_start = input_number_or_default("Input starting m", 40)
            m_end = input_number_or_default("Input final m", 400)
            m_step = input_number_or_default("Input step", 40)
            count_for_different_m(method, m_start, m_end, m_step, n)
            awaiting = False
        else:
            print(f"Incorrect graph type: {graph_type}")


def input_number_or_default(prompt, default):
    value = input(prompt + f" [default={default}]: ") or default
    return int(value)


def count_for_default_intervals(method, n, m):
    if method == Method.ExplicitFiniteDifference:
        method_impl = ExplicitFiniteDifferenceMethod(n, m, x_max, t_max)
    elif method == Method.ImplicitFiniteDifference:
        method_impl = ImplicitFiniteDifferenceMethod(n, m, x_max, t_max)
    else:
        method_impl = CrankNicolsonMethod(n, m, x_max, t_max)
    approx_values = method_impl.count()
    error = count_error(approx_values, x_max, t_max)
    show_plot(approx_values, x_max, t_max, error, METHOD_TITLES[method])


def count_for_different_n(method, n_start, n_end, n_step, m):
    errors = []
    nn = range(n_start, n_end, n_step)
    for n in nn:
        if method == Method.ExplicitFiniteDifference:
            approx_values = ExplicitFiniteDifferenceMethod(n, m, x_max, t_max).count()
        elif method == Method.ImplicitFiniteDifference:
            approx_values = ImplicitFiniteDifferenceMethod(n, m, x_max, t_max).count()
        else:
            approx_values = CrankNicolsonMethod(n, m, x_max, t_max).count()
        error = count_error(approx_values, x_max, t_max)
        errors.append(error)
    title = METHOD_TITLES[method]
    title += f"\nN = {{{n_start}, {n_start + n_step}, ..., {n_end - n_step}, {n_end}}}, M = {m}"
    title += f"\nerror(n = {n_end}) = {errors[len(errors) - 1]}"
    show_errors_plot(errors, nn, title=title, xlabel="N")


def count_for_different_m(method, m_start, m_end, m_step, n):
    errors = []
    mm = range(m_start, m_end + m_step, m_step)
    for m in mm:
        if method == Method.ExplicitFiniteDifference:
            approx_values = ExplicitFiniteDifferenceMethod(n, m, x_max, t_max).count()
        elif method == Method.ImplicitFiniteDifference:
            approx_values = ImplicitFiniteDifferenceMethod(n, m, x_max, t_max).count()
        else:
            approx_values = CrankNicolsonMethod(n, m, x_max, t_max).count()
        error = count_error(approx_values, x_max, t_max)
        errors.append(error)
    title = METHOD_TITLES[method]
    title += f"\nN = {n}, M = {{{m_start}, {m_start + m_step}, ..., {m_end - m_step}, {m_end}}}"
    title += f"\nerror(m = {m_end}) = {errors[len(errors) - 1]}"
    show_errors_plot(errors, mm, title=title, xlabel="M")


run()
