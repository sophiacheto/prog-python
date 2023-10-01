from math import sqrt


def media_arit(xs):
    soma = 0
    for i in xs:
        soma += i
    return soma / len(xs)


def desvio_padrao(xs):
    num = 0
    for i in xs:
        num += (i - media_arit(xs)) ** 2
    return sqrt(num / (len(xs) - 1))


print(desvio_padrao([4, 9, 11, 12, 17, 5, 8, 12, 14]))
