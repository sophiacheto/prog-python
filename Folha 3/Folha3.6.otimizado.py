from turtle import *


def casa(lado):
    for i in range(4):
        forward(lado)
        right(90)
    left(60)
    for i in range(2):
        forward(lado)
        right(120)


# teste
n = int(input('Qual o comprimento do lado?'))
casa(n)
