def mindiv(n):
    for d in range(2, n+1):
        if n % d == 0:
            return d


teste = int(input('N?'))
print(mindiv(teste))
