import math


def mindiv(n):
    for d in range(2, n + 1):
        if n % d == 0:
            return d
        elif d > math.sqrt(n):
            return n


teste = int(input('N?'))
print(mindiv(teste))


# def mindiv(n):
#     for d in range(2, int(math.sqrt(n))+1):
#         if n % d == 0:
#             return d
#     return n
