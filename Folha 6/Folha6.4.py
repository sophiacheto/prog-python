def ocorrencias(txt, c):
    lista = []
    count = 0
    for i in txt:
        if i == c:
            lista.append(count)
        count += 1
    return lista


print(ocorrencias('banana', 'a'))
