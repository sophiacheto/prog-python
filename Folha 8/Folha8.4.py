def collatz(n):
    lista = []
    while True:
        lista.append(n)
        if n == 1:
            return lista
        elif n % 2 == 0:
            n = n//2
        else:
            n = n*3 + 1


print(collatz(6))


def collatzrec(n, lista):
    lista.append(n)
    if n == 1:
        return lista
    elif n % 2 == 0:
        return collatzrec(n//2, lista)
    else:
        return collatzrec(n*3 + 1, lista)


print(collatzrec(6, []))


def collatzrec2(n):
    lista = []
    if n == 1:
        return lista2
    elif n % 2 == 0:
        lista2 = lista
        return lista2.append(collatzrec(n // 2)[-1])
    else:
        return lista2.append(collatzrec(n * 3 + 1)[-1])


print(collatzrec2(6))


def collatzrec(n):
    lista = lista.append(n)
    if n == 1:
        return lista
    elif n % 2 == 0:
        return collatzrec(n//2, lista)
    else:
        return collatzrec(n*3 + 1, lista)