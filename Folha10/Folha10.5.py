

def transposta(A: list[list[int]]) -> list[list[int]]:
    n = len(A)  # n linhas
    m = len(A[0])  # n colunas
    t = []
    for l in range(m):  # criar linhas
        t.append([])
        for c in range(n):
            t[l].append(A[c][l])
    return t



def transp(A):
    t = []
    num_colunas = len(A[0])
    num_linhas = len(A)
    for linha in range(num_colunas):
        t.append([])
        for coluna in range(num_linhas):
            t[linha].append(A[coluna][linha])
    return t

print(transp([[1, 2], [3, 4]]))
