def apenas_letras(txt):
    letra = ''
    caracter = ''
    for x in txt:
        if ord('A') <= ord(x) <= ord('Z') or ord('a') <= ord(x) <= ord('z') or ord(x) == ord(' '):
            letra += x
        else:
            caracter += x
    return caracter == ''



print(apenas_letras('Ola, mundo'))
