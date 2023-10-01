def classifica(p):
    if 0 <= p < 50:
        return 'insuficiente'
    elif 50 <= p < 70:
        return 'suficiente'
    elif 70 <= p < 80:
        return 'bom'
    elif 80 <= p < 90:
        return 'muito bom'
    elif 90 <= p < 100:
        return 'excelente'
    else:
        return 'inválido'


teste = int(input('Nota?'))
print(classifica(teste))
