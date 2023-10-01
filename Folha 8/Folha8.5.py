def collatz(n):
    lista = []
    while True:
        lista.append(n)
        if n == 1:
            return lista
        elif n % 2 == 0:
            n = n//2
        else:
            n = n*3 + 1


def tabcollatz():
    f = open('tabela.txt', 'w')
    f.write('%-4s %-16s \n' % ('n', 'len(collatz)'))
    for i in range(1, 1001):
        f.write('%-4s %-16s \n' % (i, len(collatz(i))))
    f.close()
