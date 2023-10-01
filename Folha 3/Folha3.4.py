Ci = int(input('Qual o seu capital inicial?'))
r = int(input('Qual a taxa de juros?')) / 100


print('Meses    Capital Final')
for n in range(6, 25):
    Cf = Ci * (1 + r/12) ** n
# print('Em', n, 'meses, seu capital final será:', Cf, 'EUR')
    print(n, '       ', Cf)

###############
#  ci = int(input('Capital inicial?'))
#  r = float(input('Juros?'))

#  print('%-8s %s' % ('Meses', 'Capital final'))
#  for n in range(6, 25):
#      print('%-8d %.2f' % (n, ci * (1 + r/12)**n))
