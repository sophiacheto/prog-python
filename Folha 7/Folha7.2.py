def media_geom(xs):
    mult = 1
    count = 0
    for i in xs:
        mult *= i
        count += 1
    return mult ** (1 / count)


