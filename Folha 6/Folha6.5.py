def repetidos(lista):
    retiradas = []
    for c in lista:
        if c in retiradas:
            return True
        retiradas.append(c)
    return False
