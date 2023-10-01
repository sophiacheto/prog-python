from turtle import *


def estrela(lado):
    for i in range(5):
        forward(lado)
        left(144)
    exitonclick()


n = int(input('Qual o comprimento do lado?'))
estrela(n)
