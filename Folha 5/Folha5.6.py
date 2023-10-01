from string import ascii_letters as letters


def apenas_letras(txt: str) -> str:
    return ''.join([c for c in txt if c in letters])


def filtra_letras(txt):
    letra = ''
    for x in txt:
        if ord('A') <= ord(x) <= ord('Z') or ord('a') <= ord(x) <= ord('z'):
            letra += x
    return letra


print(filtra_letras('Ola!, -- disse ele...'))
