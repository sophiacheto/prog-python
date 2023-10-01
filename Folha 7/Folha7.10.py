from typing import Any


def criarlinha(n):
    linha = []
    for _ in range(n):
        linha.append('')
    return linha


def criarmatriz(n):
    matriz = []
    for _ in range(n):
        matriz.append(criarlinha(n))
    return matriz


def quadrado(n: int):
    qd = criarmatriz(n)
    coluna = n // 2
    qd[0][coluna] = 1
    # agr ja tenho a minha primeira linha com o 1 no meio
    num = 1
    linha = n
    while num < n**2:
        if coluna + 1 == n and linha == 0:  # extremidade do qd
            num += 1
            linha = 1
            qd[linha][coluna] = num
        elif coluna + 1 == n:  # se eu passar da ultima coluna
            coluna = -1
        elif linha - 1 == -1:
            linha = n
        elif qd[linha-1][coluna+1] != '':  # se tiver numero no espaço seguinte
            num += 1
            linha += 1
            qd[linha][coluna] = num
        else:
            coluna += 1
            num += 1
            linha -= 1
            qd[linha][coluna] = num
    return qd


print(quadrado(5))




# I - 1 no meio da primeira linha (na linha 1, em [n//2])
# II - 2 na linha n, em [n//2 + 1]
# III - 3 na linha n-1, em [n//2 + 2] #n//2 + 2 = n
# IV - 4 na linha n-2, em [0]
# V - 5 na linha n-3, em [1]
#    na linha n-4, em [2], tem coisa !!!!!! CONTINUAR !!!!!!!!!!!!!
# VI - 6 na linha n-3+1, em [1]
# VII - 7 na linha n-3, em [2]
# VIII - 8 na linha n-4, em [3]  #n-4 = 1
# IX - 9 na linha n, em [4]
# X - 10 na linha n + 1, em
# XI -

