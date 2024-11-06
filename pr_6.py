import numpy as np

V = 16
eps = 1e-6


def f(x, y):
    return 2 * V * x + V * x * x - y


def check_y(x):
    return V * x * x


def euler(n, h, x0, y0):
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0
    for i in range(n - 1):
        x[i + 1] = x[i] + h
        y[i + 1] = y[i] + h * f(x[i], y[i])
    return x, y


def ex_euler(n, h, x0, y0):
    x = np.zeros(2 * n)
    y = np.zeros(2 * n)
    x[0] = x0
    y[0] = y0
    for i in range(2 * n - 1):
        x[i + 1] = x[i] + h / 2
        if i % 2 == 0:
            y[i + 1] = y[i] + h / 2 * f(x[i], y[i])
        else:
            y[i + 1] = y[i - 1] + h * f(x[i], y[i])
    res = y[::2]
    return x[::2], res


def pre_corr(n, h, x0, y0):
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0
    for i in range(n - 1):
        x[i + 1] = x[i] + h
        y_pred = y[i] + h * f(x[i], y[i])  # предварительный расчет
        y[i + 1] = y[i] + (h / 2) * (f(x[i], y[i]) + f(x[i + 1], y_pred))  # корректировка
    return x, y


def print_results(vx, vy):
    for x in vx:
        print(f"{x:.5f}", end="\t")
    print()

    for y in vy:
        print(f"{y:.5f}", end="\t")
    print()

    for x in vx:
        print(f"{check_y(x):.5f}", end="\t")
    print()

    for i in range(len(vy)):
        print(f"{(vy[i] - check_y(vx[i])):.5f}", end="\t")
    print()

    max_deviation = max(abs(vy - check_y(vx)))
    print(f"Максимальное отклонение: {max_deviation:.5f}")


def solve():
    n = 13
    h = 1.0
    x0 = 1
    y0 = V

    print("Метод Эйлера:")
    vx, vy1 = euler(n, h, x0, y0)
    print_results(vx, vy1)
    print()

    print("Расширенный метод Эйлера:")
    vx, vy2 = ex_euler(n, h, x0, y0)
    print_results(vx, vy2)
    print()

    print("Метод предварительного и корректирующего счета:")
    vx, vy3 = pre_corr(n, h, x0, y0)
    print_results(vx, vy3)
    print()


if __name__ == "__main__":
    solve()
