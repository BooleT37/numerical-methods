from matplotlib import pyplot as plt

from functionutils import count_exact_values

N = 1000
T = 1000


def show_plot(approx_values, x_max, t_max, error):
    exact_values = count_exact_values(N, T, x_max, t_max)
    plt.plot(approx_values, label='approximate values')
    plt.plot(exact_values, label='exact values')
    plt.xlabel('x')
    plt.ylabel('t')
    plt.text(0, 0, f"Error is {error}")
    plt.show()