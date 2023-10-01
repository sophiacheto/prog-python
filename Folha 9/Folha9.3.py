def binom(n, k):
    if n == k or k == 0:
        return 1
    else:
        return binom(n-1, k-1) + binom(n-1, k)


