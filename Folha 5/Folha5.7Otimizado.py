def inversa(txt):
    inver = ''
    for x in range(-1, -len(txt)-1, -1):
        inver += txt[x]
    return inver


def inversa2(txt: str) -> str:
    return txt[::-1]


print(inversa('Ola Mundo!'))
