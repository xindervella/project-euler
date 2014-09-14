#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt


def primesieve(n):
    l = range(n)
    l[1] = 0
    for i in range(2, int(sqrt(n)) + 1):
        if l[i]:
            l[i**2::i] = [0] * ((n - 1 - i**2) / i + 1)

    return [x for x in l if x]


if __name__ == '__main__':
    print sum(primesieve(2*10**6))
