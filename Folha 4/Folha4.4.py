def bissexto(n):
    if n % 4 == 0:
        if n % 100 == 0 and n % 400 != 0:
            return False
        else:
            return True
    else:
        return False


teste = int(input('Ano?'))
print(bissexto(teste))
