def binom(n, k):
    num = 1
    den = 1
    for x in range(n, n-k, -1):
        num *= x
    for y in range(1, k+1):
        den *= y
    return num/den


print(binom(10, 8))
