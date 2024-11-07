import numpy as np

V = 4
T = V
eps = 1e-6


def f(x):
    return 4 * V * x ** 4 - 3 * V * T * x ** 3 + 6 * V * x - 2 * V * T


def p(x):
    return x ** 2


def q(x):
    return x


def check_y(x):
    return V * x ** 2 * (x - T)


def tridiagonal_algorithm(a, b, c, d):
    n = len(a)
    p = np.zeros(n + 1)
    q = np.zeros(n + 1)
    for i in range(n):
        denom = b[i] - a[i] * p[i]
        p[i + 1] = c[i] / denom
        q[i + 1] = (a[i] * q[i] - d[i]) / denom
    res = np.zeros(n)
    res[-1] = q[n]
    for i in range(n - 2, -1, -1):
        res[i] = p[i + 1] * res[i + 1] + q[i + 1]
    return res


def print_results(vx, vy):
    max_deviation = 0
    max_deviation_index = 0

    print(f"{'Индекс':<10}{'x':<10}{'y':<20}{'Отклонение':<20}")
    for i in range(len(vx)):
        deviation = abs(vy[i] - check_y(vx[i]))
        print(f"{i:<10}{vx[i]:<10.5f}{vy[i]:<20.5f}{deviation:<20.5f}")

        # Update maximum deviation
        if deviation > max_deviation:
            max_deviation = deviation
            max_deviation_index = i

    # Output maximum deviation information
    print("\nМаксимальное отклонение:")
    print(f"Индекс: {max_deviation_index}")
    print(f"x: {vx[max_deviation_index]:.10f}, y: {vy[max_deviation_index]:.10f}, Отклонение: {max_deviation:.10f}")


def solve():
    n = 1000000
    l, r = 0, T
    h = (r - l) / n
    vx = [l + i * h for i in range(n + 1)]

    a = np.zeros(n - 1)
    b = np.zeros(n - 1)
    c = np.zeros(n - 1)
    d = np.zeros(n - 1)

    for i in range(n - 1):
        x = vx[i + 1]
        a[i] = 1 / h ** 2 - p(x) / (2 * h)
        b[i] = -(-2 / h ** 2 + q(x))
        c[i] = 1 / h ** 2 + p(x) / (2 * h)
        d[i] = f(x)

    a[0] = 0
    c[-1] = 0
    vy = tridiagonal_algorithm(a, b, c, d)
    vy = np.concatenate(([0], vy, [0]))  # add boundary conditions at both ends
    print_results(vx, vy)


solve()
