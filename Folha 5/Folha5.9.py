# def inverter(txt):
#    inver = ''
#    for x in range(len(txt)-1, -1, -1):
#        inver += txt[x]
#    return inver


def inverter(txt):
    return txt[::-1]


def filtra_letras(txt):
    letra = ''
    for x in txt:
        if ord('A') <= ord(x) <= ord('Z') or ord('a') <= ord(x) <= ord('z'):
            letra += x
    return letra


def palindromo(txt):
    txt = txt.lower()
    txt = filtra_letras(txt)
    inversa = inverter(txt)
    return inversa == txt


print(palindromo("testeee!!!!!"))
