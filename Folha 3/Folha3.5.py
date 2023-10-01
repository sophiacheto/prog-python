from turtle import *


def triangulo(lado):
    for i in range(3):
        forward(lado)
        left(120)


# teste
n = int(input('Qual o comprimento do lado?'))
print(triangulo(n))
