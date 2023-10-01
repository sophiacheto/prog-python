from math import sqrt


def area_triangulo(a, b, c):
    s = (a + b + c) / 2
    A = sqrt(s * (s - a) * (s - b) * (s - c))
    return A
