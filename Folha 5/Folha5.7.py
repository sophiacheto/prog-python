def inversa(txt):
    inver = ''
    for x in range(len(txt)-1, -1, -1):
        inver += txt[x]
    return inver


print(inversa('Ola Mundo!'))
