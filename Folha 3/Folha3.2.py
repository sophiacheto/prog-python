import math

gr = int(input('Graus?'))
mins = int(input('Minutos?'))
sec = int(input('Segundos?'))


graus = gr + mins / 60 + sec / 3600
rad = (2 * math.pi * graus) / 360

print(rad, 'radianos')
