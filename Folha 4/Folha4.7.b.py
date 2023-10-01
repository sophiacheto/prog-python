def primo(n):
    d = 2
    while n != 1 and n % d != 0:
        d += 1
    if d == n:
        return 'True'
    else:
        return 'False'

# def primo(n):
#     d = 2
#     while n != 1 and n%d != 0:
#         d += 1
#     return d == n


teste = int(input('N?'))
print(primo(teste))
