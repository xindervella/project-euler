#!/usr/bin/env python
# -*- coding: utf-8 -*-


def factors(n):
    f = 1
    while f ** 2 <= n:
        if not n % f:
            yield f
            yield n / f
        f += 1


def primefactors(n):
    f = 2
    while f ** 2 <= n:
        while not n % f:
            yield f
            n /= f
        f += 1
    if n > 1:
        yield n

from collections import defaultdict
def uniprimefactors(n):
    d = defaultdict(int)
    for i in primefactors(n):
        d[i] += 1
    return dict(d)
