import math

import numpy as np

from AlternatingDirectionMethod import AlternatingDirectionMethod
from functionutils import count_errors_for_layers
from gui import show_plot, show_errors_plot

x_max = math.pi * 2
t_max = 10
n_default = 10
m_default = 40


def run():
    while True:
        prompt_method_params()
        print("\n\n")


def prompt_method_params():
    awaiting = True
    while awaiting:
        print("[1] for 3D graph u(x, y, t)\n"
              "[2] for error(n)\n"
              "[3] for error(m)\n")
        graph_type = input_number_or_default("Input graph type", 1)
        if graph_type == 1:
            n = input_number_or_default("Input n", n_default)
            m = input_number_or_default("Input m", m_default)
            count_for_default_intervals(n, m)
            awaiting = False
        elif graph_type == 2:
            n_start = input_number_or_default("Input starting n", n_default)
            n_end = input_number_or_default("Input final n", 100)
            n_step = input_number_or_default("Input step", 10)
            m = input_number_or_default("Input m", m_default)
            count_for_different_n(n_start, n_end, n_step, m)
            awaiting = False
        elif graph_type == 3:
            n = input_number_or_default("Input n", n_default)
            m_start = input_number_or_default("Input starting m", m_default)
            m_end = input_number_or_default("Input final m", 400)
            m_step = input_number_or_default("Input step", 40)
            count_for_different_m(m_start, m_end, m_step, n)
            awaiting = False
        else:
            print(f"Incorrect graph type: {graph_type}")


def input_number_or_default(prompt, default):
    value = input(prompt + f" [default={default}]: ") or default
    return int(value)


def count_for_default_intervals(n, m):
    approx_values = AlternatingDirectionMethod(n, m, x_max, t_max).count()
    errors = count_errors_for_layers(approx_values, x_max, t_max)
    show_plot(approx_values, x_max, t_max, errors)


def count_for_different_n(n_start, n_end, n_step, m):
    errors = []
    nn = range(n_start, n_end, n_step)
    for n in nn:
        approx_values = AlternatingDirectionMethod(n, m, x_max, t_max).count()
        errors = count_errors_for_layers(approx_values, x_max, t_max)
        error = np.max(errors)
        errors.append(error)
    title = "Метод переменных направлений"
    title += f"\nN = {{{n_start}, {n_start + n_step}, ..., {n_end - n_step}, {n_end}}}, M = {m}"
    title += f"\nerror(n = {n_end}) = {errors[len(errors) - 1]}"
    show_errors_plot(errors, nn, title=title, xlabel="N")


def count_for_different_m(m_start, m_end, m_step, n):
    errors = []
    mm = range(m_start, m_end + m_step, m_step)
    for m in mm:
        approx_values = AlternatingDirectionMethod(n, m, x_max, t_max).count()
        errors = count_errors_for_layers(approx_values, x_max, t_max)
        error = np.max(errors)
        errors.append(error)
    title = "Метод переменных направлений"
    title += f"\nN = {n}, M = {{{m_start}, {m_start + m_step}, ..., {m_end - m_step}, {m_end}}}"
    title += f"\nerror(m = {m_end}) = {errors[len(errors) - 1]}"
    show_errors_plot(errors, mm, title=title, xlabel="M")


# run()
count_for_default_intervals(n_default, m_default)