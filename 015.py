#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def memoized(f):
    m = {}
    l = lambda *k: m[k] if k in m else m.setdefault(k, f(*k))
    l.cached = m
    return l

from functools import lru_cache

# if python2
# @memoized

# python 3 only
@lru_cache(maxsize=None)
def a(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        return a(x-1, y) + a(x, y-1)

print(a(20, 20))
