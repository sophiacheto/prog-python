def bagdiff(xs: list, ys: list) -> list:
    """
    >>> bagdiff([3, 2, 1, 2, 3, 3], [2, 2, 3])
    [1, 3, 3]
    >>> bagdiff([3, 3, 2], [1, 2, 3])
    [3]
    """
    for n in ys:
        if n in xs:
            xs.remove(n)
    return xs
