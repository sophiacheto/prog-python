from turtle import *


def draw_tree(n, angle, ratio, size, esp):
    pensize(esp)
    forward(ratio*size)  # desenhar uma linha
    if n > 0:  # caso recursivo
        nsize = (1-ratio)*size
        esp *= 0.8
        (x, y) = position()  # guardar posição
        h = heading()  # e orientação
        left(angle)
        draw_tree(n-1, angle, ratio, nsize, esp)
        penup()  # não desenhar
        goto(x, y)  # repor a posição
        setheading(h)  # e orientação
        pendown()  # voltar a desenhar
        right(angle)
        draw_tree(n-1, angle, ratio, nsize, esp)


draw_tree(6, 30, 0.3, 150, 4)