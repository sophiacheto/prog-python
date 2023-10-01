def repetidos(lista):
    retiradas = []
    for c in lista:
        if c in retiradas:
            return True
        retiradas.append(c)
    return False


def acertos(chave: list, aposta: list) -> int:
    assert type(chave) == list and type(aposta) == list, 'tipo inválido'
    assert not repetidos(chave) and not repetidos(aposta), 'itens repetidos'
    acert = [c for c in chave if c in aposta]
    return len(acert)


print(acertos([25, 49, 27, 3, 17, 33], [33, 9, 19, 49, 1, 7]))
