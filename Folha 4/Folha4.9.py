import random


def somadoisdados(k):
    soma = 0
    for i in range(10000):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        if d1 + d2 == k:
            soma += 1
    return soma / 10000


for n in range(2, 13):
    print('A frequência do resultado', n, 'foi', somadoisdados(n))
