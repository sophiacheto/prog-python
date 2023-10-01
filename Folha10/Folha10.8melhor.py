def linha(n, grelha):
    linha = grelha[n]
    linha2 = list(linha)
    linha2.sort()
    return linha2


def coluna(n, grelha):
    coluna = []
    for linha in grelha:
        coluna.append(linha[n])
    coluna2 = list(coluna)
    coluna2.sort()
    return coluna2


def bloco_n_da_m_linha(n, m, grelha):
    bloco = []
    for x in grelha[m*3:(m*3)+3]:  # para cada elemento nas 3 linhas escolhidas
        bloco.extend(x[n*3:(n*3)+3])
    bloco.sort()
    return bloco


def sudoku(grelha):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in range(9):
        if linha(n, grelha) != nums or coluna(n, grelha) != nums:
            print(n, linha(n, grelha), coluna(n, grelha))
            return False
    for i in range(3):
        for j in range(3):
            if bloco_n_da_m_linha(i, j, grelha) != nums:
                return False
    return True
