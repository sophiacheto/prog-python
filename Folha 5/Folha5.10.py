def rem_espacos(txt):
    nova = ''
    for i in range(len(txt)):
        if txt[i] == ' ' and txt[i-1] == ' ':
            nova = nova
        else:
            nova += txt[i]
    return nova


print(rem_espacos(' Ola, mundo!       ! '))


def rem_espacos_correta(txt):
    nova = txt[0]
    for i in range(1, len(txt)):
        if txt[i] == ' ' and txt[i - 1] == ' ':
            nova = nova
        else:
            nova += txt[i]
    return nova



