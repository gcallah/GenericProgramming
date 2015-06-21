"""
quot_remain.py
Code from chapter 4 of _From Mathematics to Generic Programming_.
Converted from C++ to Python by Gene Callahan.
"""


def largest_doubling(a, b):
    assert(b != 0)
    while a - b >= b:
        b = b + b
    return b


def quotient_remainder(a, b):
    assert(b > 0)
    if a < b:
        return (0, a)
    c = largest_doubling(a, b)
    print("calculating for %i and %i with doubling of %i" % (a, b, c))
    n = 1
    a = a - c
    while c != b:
        c = c // 2
        n = n + n
        if c <= a:
            a = a - c
            n = n + 1

    return (n, a)
