def factorial(n):
    if n < 0:
        raise ValueError
    elif type(n) == float:  # isinstance(n, float)
        raise TypeError
    r = 1
    while n > 1:
        r = r*n
        n = n-1
    return r


print(factorial(7.5))

