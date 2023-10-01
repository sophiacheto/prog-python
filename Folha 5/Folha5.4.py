# nivel facil hihi

def fatorial(n):
    fat = 1
    for x in range(n, 0, -1):
        fat *= x
    return fat


def binom(n, k):
    bin = fatorial(n)/(fatorial(k) * fatorial(n-k))
    return bin


print(binom(10, 0))
