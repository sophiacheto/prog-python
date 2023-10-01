def palindromo(txt):
    txt = txt.lower()
    inversa = ''
    for x in range(len(txt)-1, -1, -1):
        inversa += txt[x]
    return inversa == txt


print(palindromo('teste'))


def palindromomelhorado(txt):
    txt = txt.lower()
    return txt == txt[::-1]


print(palindromomelhorado('reviver'))
