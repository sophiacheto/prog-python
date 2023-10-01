def media(valores):
    if type(valores) != list:
        raise TypeError
    elif not valores:
        raise ValueError
    else:
        return sum(valores)/len(valores)


print(media([]))
