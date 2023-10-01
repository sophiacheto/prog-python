from turtle import *


def espiral():
    lado = 5
    while lado < 500:
        forward(lado)
        right(90)
        lado += 2


espiral()
