def apenas_letras(txt):
    txt = txt.lower()
    caracter = ''
    for x in txt:
        if (ord(x) < ord('a') or ord(x) > ord('z')) and ord(x) != ord(' '):
            caracter += x
    return caracter == ''


print(apenas_letras('abracadabra'))
