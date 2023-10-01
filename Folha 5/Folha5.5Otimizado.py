def apenas_letras(txt):
    caracter = ''
    for x in txt:
        if (ord(x) < ord('A') or ord('Z') < ord(x) < ord('a') or ord(x) > ord('z')) and ord(x) != ord(' '):
            caracter += x
    return caracter == ''


print(apenas_letras('Ola, mundo'))
