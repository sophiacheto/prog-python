def maislonga(fich):
    f = open(fich, "r", encoding="utf-8")
    palavra = ''
    while True:  # repetir
        linha = f.readline()  # uma nova linha
        if linha == "":  # fim do ficheiro?
            break
        linha = linha.split()  # a palavra ocorre?
        for w in linha:
            if len(w) > len(palavra):
                palavra = w
    # fim do ciclo
    f.close()
    return len(palavra)


print(maislonga('lusiadas_canto.txt'))
