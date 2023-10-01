def mindiv(n):
    for d in range(2, (n+1)):
        if (n % d) == 0:
            return d


def primo(n):
    if mindiv(n) == n:
        return 'true'
    else:
        return 'false'


# def primo(n):
#   return n == mindiv(n)


teste = int(input('N?'))
print(primo(teste))
