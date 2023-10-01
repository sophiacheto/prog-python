from turtle import *


def friso(n, lado):
    for i in range(n):
        forward(lado)
        left(90)
        for _ in range(2):
            forward(lado)
            right(90)
        forward(lado)
        left(90)


rep = int(input('Quantas ameias?'))
tam = int(input('Qual o tamanho de cada segmento?'))
print(friso(rep, tam))
