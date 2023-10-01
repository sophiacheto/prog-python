from turtle import *


def casa(lado):
    for i in range(4):
        forward(lado)
        left(90)
    left(90)
    forward(lado)
    right(90)
    for i in range(3):
        forward(lado)
        left(120)


# teste
n = int(input('Qual o comprimento do lado?'))
print(casa(n))
