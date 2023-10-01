def linhan(A, n):
    return A[n]


def colunan(A, n):
    coluna = []
    for linha in A:
        coluna.append(linha[n-1])
    return coluna


def diagonal(A):
    diag = []
    count = 0
    for linha in A:
        diag.append(linha[count])
        count += 1
    return diag


def magico(A):
    somalinha1 = sum(A[0])
    for n in range(1, len(A)):
        somalinhan = sum(A[n])
        if somalinha1 != somalinhan:
            return False
    somacoluna1 = sum(colunan(A, 0))
    for n in range(1, len(A)):
        somacolunan = sum(colunan(A, n))
        if somacoluna1 != somacolunan:
            return False
    somadiag = sum(diagonal(A))
    return somadiag == somacoluna1 == somalinha1


print(linhan([[2, 7, 6], [9, 5, 1], [4, 3, 8]], 1))