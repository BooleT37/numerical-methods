import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from functionutils import count_exact_values
from utils import inclusive_range


def show_plot(approx_values, x_max, t_max, error):
    n = approx_values.shape[1] - 1
    m = approx_values.shape[0] - 1
    exact_values = count_exact_values(n, m, x_max, t_max)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    Axes3D.plot_surface(ax, *create_grid(x_max, t_max, n, m, exact_values), color='royalblue')
    Axes3D.plot_surface(ax, *create_grid(x_max, t_max, n, m, approx_values), color='orangered')

    ax.set_xlabel('x')
    ax.set_ylabel('t')
    # ax.legend(['exact values', 'approx_values'])
    ax.set_title(f"Error is {error}")

    plt.show()


def create_grid(x_max, t_max, n, m, zz):
    h = x_max / n
    tau = t_max / m
    xx = np.array(inclusive_range(0, x_max, h))
    tt = np.array(inclusive_range(0, t_max, tau))
    xx, tt = np.meshgrid(xx, tt)
    return xx, tt, zz
