from turtle import *


def espiral():
    lado = 5
    for i in range(0, 92):
        forward(lado)
        right(89)
        lado += 3


espiral()
