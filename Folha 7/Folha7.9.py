def tempo(n):
    horas = n//3600
    minutos = (n % 3600)//60
    segundos = (n % 3600) % 60
    return '%02d:%02d:%02d' % (horas, minutos, segundos)


print(tempo(121))
