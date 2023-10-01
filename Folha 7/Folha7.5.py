def intervalo(xs, a, b):
    interv = []
    for i in xs:
        if a <= i <= b:
            interv.append(i)
    return interv


# OU (se for só pra contar a qtd)

def qtd_intervalo(xs, a, b):
    qtd = 0
    for i in xs:
        if a <= i <= b:
            qtd += 1
    return qtd
