def ordem(x: str) -> int:
    if ord('a') <= ord('x') <= ord('z'):
        return ord(x) - ord('a') + 1
    elif ord('A') < ord('x') < ord('Z'):
        return ord(x) - ord('A') + 1


def letra(y: int) -> str:
    numeroletra = y % 26 + 96
    return chr(numeroletra)


def vigenere(chave, mensagem):
    cifra = ''
    recorrencia = 0
    for c in mensagem:
        if ordem('a') <= ordem(c) <= ordem('z'):
            recorrencia += 1
            ordemnachave = recorrencia % len(chave)
            k = ordem('z') - ordem(chave[ordemnachave - 1]) + 1
            novaletra = letra(ordem(c) - k)
            cifra += novaletra
        else:
            cifra += c
    return cifra


print(vigenere('luar', 'ataque de madrugada!'))
