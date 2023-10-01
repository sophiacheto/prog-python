def remadj(xs):
    """
    >>> remadj([2,2,3,1,4,4])
    [2, 3, 1, 4]
    >>> remadj(['a','b','b','b','a'])
    ['a', 'b', 'a']
    """
    nova = list(xs)
    for i in range(0, len(xs)-1):
        if xs[i] == xs[i+1]:
            del nova[i]
    return nova
