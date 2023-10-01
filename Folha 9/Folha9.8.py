from turtle import *


def sierpinski(n, lado):
    if n == 0:
        for _ in range(3):
            forward(lado)
            left(120)
    else:
        for _ in range(3):
            forward(lado)
            left(120)
            sierpinski(n-1, lado/2)


sierpinski(2, 100)
