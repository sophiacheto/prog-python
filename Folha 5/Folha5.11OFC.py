import string

def vigenere(chave, mensagem):
    cifra = ''
    rec = 0
    for c in mensagem:
        if c in string.ascii_letters:
            rec += 1
            ordem_na_chave = rec % len(chave)
            letra_na_chave = chave[ordem_na_chave - 1]
            k = ord('z') - ord(letra_na_chave) + 1
            if ord(c) - k < 97:
                caracter = ord(c) - k + 26  # da certo pro 'a'
            else:
                caracter = ord(c) - k  # da certo pro 't'
            nova_letra = chr(caracter)
            cifra += nova_letra
        else:
            cifra += c
    return cifra


print(vigenere('luar', 'ataque de madrugada!'))
