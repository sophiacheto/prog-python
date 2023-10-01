from string import *


def temalg(txt):
    alg = ''
    for c in txt:
        if c in digits:
            alg += c
    return alg != ''


def temmaius(txt):
    maius = ''
    for c in txt:
        if c in ascii_uppercase:
            maius += c
    return maius != ''


def temminus(txt):
    minus = ''
    for c in txt:
        if c in ascii_lowercase:
            minus += c
    return minus != ''


def forte(passwd):
    return len(passwd) >= 8 and temalg(passwd) and temminus(passwd) and temmaius(passwd)

