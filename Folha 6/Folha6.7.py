def unidade(n):
    lista = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    return lista[n]


def dezena(n):
    lista = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    return lista[n]


def centena(n):
    lista = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos',
             'oitocentos', 'novecentos']
    return lista[n]


def texto(n):
    if 10 <= n <= 19 or n == 0:
        lista = ['zero', '', '', '', '', '', '', '', '', '', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
                 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
        return lista[n]
    elif len(str(n)) == 1:
        return unidade(n)
    elif len(str(n)) == 2:
        return dezena(int(str(n)[0])) + ' e ' + unidade(int(str(n)[1]))
    elif len(str(n)) == 3:
        return centena(int(str(n)[0])) + ' e ' + dezena(int(str(n)[0])) + ' e ' + unidade(int(str(n)[1]))


print(texto(222))
