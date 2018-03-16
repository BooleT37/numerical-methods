import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import msvcrt

from functionutils import count_exact_values
from utils import inclusive_range


def show_plot(approx_values, x_max, t_max, errors):
    n = approx_values.shape[1] - 1
    m = approx_values.shape[0] - 1
    tau = t_max / m
    exact_values = count_exact_values(n, m, x_max, t_max)

    print(f"Total error is {max(errors)}\n")

    k = 0
    t = 0
    print(f"Временной разрез {k} (t = {t})")
    show_plot_for_layer(approx_values[k], exact_values[k], errors[k], x_max, n, m, t, tau)
    while k <= m:
        k += 1
        t = tau * k
        print(f"Временной разрез {k} (t = {t})")
        show_plot_for_layer(approx_values[k], exact_values[k], errors[k], x_max, n, m, t, tau)


def show_plot_for_layer(approx_values, exact_values, error, x_max, n, m, t, tau):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    Axes3D.plot_surface(ax, *create_grid(x_max, n), approx_values, color='royalblue')
    Axes3D.plot_surface(ax, *create_grid(x_max, n), exact_values, color='orangered')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    h = "{:.2f}".format(x_max / n)
    ax.set_title(f"Метод переменных направлений\n"
                 f"t ={t}, n = {n} (h = {h}), m = {m} (tau = {tau})\nError is {error}")
    plt.show()


def create_grid(x_max, n):
    h = x_max / n
    xx = np.array(inclusive_range(0, x_max, h))
    xx, yy = np.meshgrid(xx, xx)
    return xx, yy


def show_errors_plot(errors, values, **kwargs):
    plt.plot(values, errors)
    plt.title(kwargs["title"])
    plt.xlabel(kwargs["xlabel"])
    plt.ylabel("error")
    plt.show()
