def comprimento_medio(fich):
    f = open(fich, "r", encoding="utf-8")
    soma_letras = 0
    soma_palavras = 0
    while True:  # repetir
        linha = f.readline()  # uma nova linha
        if linha == "":  # fim do ficheiro?
            break
        linha = linha.split()
        for w in linha:
            soma_letras += len(w)
            soma_palavras += 1
    # fim do ciclo
    f.close()
    return soma_letras / soma_palavras


print(comprimento_medio('lusiadas_canto.txt'))
