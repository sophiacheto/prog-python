def bissexto(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        return n


for i in range(2000, 2021):
    if bissexto(i) is not None:
        print(bissexto(i))

# ou:
for n in range(2000, 2021):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        print(n)
