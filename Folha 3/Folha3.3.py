import math


def radianos(g, m, s):
    graus = g + m / 60 + s / 3600
    rad = (2 * math.pi * graus) / 360
    return rad


# testando
gr = int(input('Graus?'))
mins = int(input('Minutos?'))
sec = int(input('Segundos?'))

print(radianos(gr, mins, sec))
