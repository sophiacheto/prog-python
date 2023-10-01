def triang_sup(A: list[list[float]], eps: float) -> bool:
    for i in range(len(A)):
        for j in range(len(A)):
            if j < i and A[i][j] >= eps:
                return False
    return True
