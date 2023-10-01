def media_arit(xs):
    soma = 0
    count = 0
    for i in xs:
        soma += i
        count += 1
    return soma / count


def media_arit2(xs):
    return sum(xs)/len(xs)
