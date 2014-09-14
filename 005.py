#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce


def prime_factor(n):
    f = 2
    while f ** 2 <= n:
        while not n % f:
            yield f
            n /= f
        f += 1
    if n > 1:
        yield n


def product(l):
    return reduce(lambda x, y: x*y, l)


def max_power(n, top):
    i = 0
    while True:
        top /= n
        i += 1
        if top < n:
            return i

if __name__ == '__main__':
    from itertools import chain
    TOP = 20
    print product([i ** max_power(i, TOP)
                  for i in set(chain(*[prime_factor(i) for i in range(TOP)]))])
