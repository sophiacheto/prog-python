def decompor(quantia: int) -> list[int]:
    '''
    >>> decompor(488)
    [200, 200, 50, 20, 10, 5, 2, 1]
    >>> decompor(468)
    [200, 200, 50, 10, 5, 2, 1]
    >>> decompor(448)
    [200, 200, 20, 20, 5, 2, 1]
    >>> decompor(1448)
    [200, 200, 200, 200, 200, 200, 200, 20, 20, 5, 2, 1]
    >>> decompor(348)
    [200, 100, 20, 20, 5, 2, 1]
    >>> decompor(345)
    [200, 100, 20, 20, 5]
    '''
    lista = []
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    for moeda in moedas:
        while moeda <= quantia:
            lista.append(moeda)
            quantia -= moeda
    return lista


print(decompor(345))