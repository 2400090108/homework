def f(x):
    return x ** 3 - 5 * x ** 2 + 10 * x - 80


def df(x):
    return 3 * x ** 2 - 10 * x + 10


def newton_method(x0, tol=1e-9, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        x -= fx / dfx
    return x


root2 = newton_method(3)
print(f"{root2:.9f}")
