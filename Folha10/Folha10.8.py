def sudoku(grelha):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in range(len(grelha)):
        coluna = []
        for linha in grelha:
            linha2 = list(linha)
            linha2.sort()
            if linha2 != nums:
                return False
            coluna.append(linha[n])
        coluna.sort()
        if coluna != nums:
            return False
    # até aqui funciona
    for k in range(0, 7, 3):
        for j in range(0, 7, 3):
            bloco = [grelha[j][k:k+3], grelha[j+1][k:k+3], grelha[j+2][k:k+3]]
            bl = []
            for aaa in bloco:
                for iii in aaa:
                    bl.append(iii)
            bl.sort()
            if bl != nums:
                return False
    return True


'''
    bloco = [grelha[3][:3], grelha[4][:3], grelha[5][:3]]
    bloco = [grelha[6][:3], grelha[7][:3], grelha[8][:3]]
    blocooo = [grelha[0][3:6], grelha[1][3:6], grelha[2][3:6]]
    [6:9]




    z = 0
    for y in range(0, 10, 3):
        blocos = []
        for i in range(y, y + 3): # linha de blocos
            for c in range(z, z + 3):
                blocos.append(grelha[i][c])
            z += 3
        blocos.sort()
        if blocos != nums:
            return False
    return True

'''
print(sudoku([[2, 5, 8, 7, 3, 6, 9, 4, 1], [6, 1, 9, 8, 2, 4, 3, 5, 7], [4, 3, 7, 9, 1, 5, 2, 6, 8], [3, 9, 5, 2, 7, 1, 4, 8, 6], [7, 6, 2, 4, 9, 8, 1, 3, 5], [8, 4, 1, 6, 5, 3, 7, 2, 9], [1, 8, 4, 3, 6, 9, 5, 7, 2], [5, 7, 6, 1, 4, 2, 8, 9, 3], [9, 2, 3, 5, 8, 7, 6, 1, 4]]))
