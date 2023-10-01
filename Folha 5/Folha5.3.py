def raiz(q, eps):
    x0 = q/2
    x = (x0 + q/x0) / 2
    while abs(x - x0) > eps:
        x0 = x
        x = (x + q/x) / 2
    return x


print(raiz(5, 0.1 ** 30))
