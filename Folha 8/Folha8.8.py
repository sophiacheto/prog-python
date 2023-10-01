from string import *


def anagramas(txt1, txt2):
    lista1 = [i for i in txt1.lower() if i in ascii_letters]
    lista2 = [c for c in txt2.lower() if c in ascii_letters]
    lista1.sort()
    lista2.sort()
    return lista2 == lista1


print(anagramas("Ataque ao amanhecer", "Ataque ao anoitecer"))
