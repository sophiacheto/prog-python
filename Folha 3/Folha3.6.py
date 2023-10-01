from turtle import *


def casa(lado):
    for i in range(6):
        forward(lado)
        left(90)
    right(60)
    for i in range(2):
        forward(lado)
        left(120)


#teste
n = int(input('Qual o comprimento do lado?'))
casa(n)


