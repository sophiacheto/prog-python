def leibniz(k: int) -> float:
    parcela = 0
    for n in range(k):
        parcela += ((-1) ** n) / (2 * n + 1)
    return 4 * parcela


teste = int(input('K?'))
print(leibniz(teste))
