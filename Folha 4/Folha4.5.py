def bissexto(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        return 'true'
    else:
        return 'false'


for i in range(2000, 2020):
    if bissexto(i) == 'true':
        print(i)
