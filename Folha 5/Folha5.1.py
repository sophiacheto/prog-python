def triangular(k):
    x = 1
    sucessor = 1
    while x < k:
        sucessor += 1
        x = x + sucessor
    return x == k


print(triangular(4097))


def triangular2(k):
    n = 0
    soma = 0
    while n <= k:
        soma += n
        n += 1
        if soma == k:
            return True
    return False
