def dup_vogais(txt):
    nova = ''
    for i in txt:
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
            nova += 2 * i
        else:
            nova += i
    return nova
