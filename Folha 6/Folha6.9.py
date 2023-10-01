from random import randint


def repetidos(lista):
    retiradas = []
    repetidas = []
    for c in lista:
        if c in retiradas:
            repetidas.append(c)
        retiradas.append(c)
    return repetidas


def aniversarios(n):
    datas = []
    for _ in range(n):
        datas.append(randint(1, 365))
    return len(repetidos(datas))/n


def prob(n):
    sum = 0
    for _ in range(10000):
        sum += aniversarios(n)
    return sum/1000


print(prob(23))
