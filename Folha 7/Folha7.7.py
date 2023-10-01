from math import log

print('%2s %7s' % ('x', 'log(x)'))
for x in range(1, 11):
    print('%2d %.6f' % (x, log(x, 10)))
