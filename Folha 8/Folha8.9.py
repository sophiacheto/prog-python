from string import ascii_uppercase


def morse(txt):
    dic = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
           'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
           'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'y': '-.--',
           'Z': '--..'}
    mors = []
    for c in txt:
        if c in ascii_uppercase:
            mors.append(dic[c])
    return ' '.join(mors)


print(morse('ABC!'))
