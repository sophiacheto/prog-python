def prod_interno(xs, ys):
    prod = 0
    for i in range(len(xs)):
        prod += xs[i] * ys[i]
    return prod


print(prod_interno((3, 2, 4), (2, 3, 5)))
