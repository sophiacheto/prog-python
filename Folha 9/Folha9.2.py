def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


def coprimos(n):
    cop = []
    for i in range(1, n):
        if mdc(i, n) == 1:
            cop.append(i)
    return cop


print(coprimos(14))
