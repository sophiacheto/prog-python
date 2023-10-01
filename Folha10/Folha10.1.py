import doctest
doctest.testmod()


def mediana(a: int, b: int, c: int) -> int:
    '''teste
    >>> mediana(3, 1, 2)
    2
    >>> mediana(1, 3, 3)
    3
    >>> mediana(2, 1, 3)
    2
    '''
    num = [a, b, c]
    num.sort()
    return num[1]
