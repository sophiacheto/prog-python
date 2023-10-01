def fatorial(n):
    fat = 1
    for x in range(n, 0, -1):
        fat *= x
    return fat


def binom(n, k):
    bin = fatorial(n) // (fatorial(k) * fatorial(n - k))
    return bin


def pascal(n):
    linha = []
    for i in range(n+1):
        linha.append(binom(n, i))
    return linha


for c in range(10):
    print(pascal(c))
