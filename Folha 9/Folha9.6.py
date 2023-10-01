from turtle import *


def koch(n: int, size: float):
    if n == 0:  # caso base
        forward(size)
    else:  # caso geral
        for angle in [60, -120, 60, 0]:
            koch(n-1, size/3)
            left(angle)


def floco(n, size):
    for i in range(3):
        koch(n, size)
        right(120)
    exitonclick()


# floco(3, 100)


def flocomelhorado(n, size):
    speed(200)
    for i in range(6):
        koch(n, size)
        left(60)
    exitonclick()


flocomelhorado(3, 150)
