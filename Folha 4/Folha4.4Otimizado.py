def bissexto(n):
    if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
        return True
    else:
        return False


def bissextonovo(n):
    return n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)


print(bissexto(1000))