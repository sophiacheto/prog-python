def aprox(q, n):
    x = q/2
    for i in range(n):
        x = (x + q/x) / 2
    return x


print(aprox(5, 1000))
