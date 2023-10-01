def triangulo(a, b, c):
    if a == b == c:
        return 'equilatero'
    elif a != b and b != c and a != c:
        return 'escaleno'
    else:
        return 'isosceles'


testea = int(input('a?'))
testeb = int(input('b?'))
testec = int(input('c?'))

print(triangulo(testea, testeb, testec))


