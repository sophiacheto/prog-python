def palindromo(txt):
    txt = filtra_letras(txt)
    if txt == '' or len(txt) == 1:
        return True
    elif txt[0] != txt[-1]:
        return False
    else:
        return palindromo(txt[1:-1])


def filtra_letras(txt):
    letra = ''
    txt = txt.lower()
    for x in txt:
        if ord('A') <= ord(x) <= ord('Z') or ord('a') <= ord(x) <= ord('z'):
            letra += x
    return letra


print(palindromo('Amora me tem aroma.'))
