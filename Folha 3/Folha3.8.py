from turtle import *


def poligono(n, lado):
    if n >= 3:
        for i in range(n):
            forward(lado)
            ang_int = (n - 2) * 180 / n
            left(180 - ang_int)
    else:
        print('O número de lados deve ser maior que 2')


nl = int(input('Qual o número de lados?'))
cl = int(input('Qual o comprimento dos lados?'))
print(poligono(nl, cl))
