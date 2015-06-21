"""
mult.py
Code from chapter 2 of _From Mathematics to Generic Programming_.
Implements Egyptian multiplication.
Converted from C++ to Python by Gene Callahan.
"""


def odd(n):
    return n & 0x1


def half(n):
    return n >> 1


def multiply(n, a):
        if n == 1:
            return a
        return mult_acc(a, n - 1, a)


def mult_acc(r, n, a):
    if odd(n):
        r = r + a
        if n == 1:
            return r
    return mult_acc(r, half(n), a + a)
