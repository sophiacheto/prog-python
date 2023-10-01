def algarismos(n):
    alg = 1
    while n // 10 > 0:
        alg += 1
        n = n / 10
    return alg


teste = float(input('Número?'))
print(algarismos(teste))


# def algarismos2(n):
#    return len(str(n))
