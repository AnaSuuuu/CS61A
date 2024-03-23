def every_m_ints_to(n, m):
    i = 0
    while (i <= n):
        yield i
        i += m

def every_3_ints_to_10():
    for item in every_m_ints_to(10, 3):
        yield item

def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    ans = []
    for i in range(4):
        kdl = g()
        tmp = []
        for j in range(i + 1):
            tmp += [next(kdl)]
        ans += [tmp]
    return ans


