from string import ascii_letters


def palavras(txt):
    letras = ''
    for i in txt:
        if i in ascii_letters or i == ' ':
            letras += i
    letras = letras.split()
    return letras
