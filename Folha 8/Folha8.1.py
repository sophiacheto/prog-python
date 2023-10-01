def contar(palavra, fich):
    f = open(fich, "r", encoding="utf-8")
    linhas = 0
    while True:  # repetir
        linha = f.readline()  # uma nova linha
        if linha == "":  # fim do ficheiro?
            break
        if palavra in linha:  # a palavra ocorre?
            linhas += 1
    # fim do ciclo
    f.close()
    return linhas


print(contar('armas', 'lusiadas_canto.txt'))
