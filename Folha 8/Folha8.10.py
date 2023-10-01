def pontua(chave, tentativa):
    pont1 = 0
    pont2 = 0
    for i in range(len(tentativa)):
        if tentativa[i] in chave:
            if tentativa[i] == chave[i]:
                pont1 += 1
            else:
                pont2 += 1
    return pont1, pont2


