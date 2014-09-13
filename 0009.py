#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt


def pythagorean(n):
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            square_c = a**2 + b**2
            c = int(sqrt(square_c))
            if c**2 == square_c and c <= n:
                yield (a, b, c)

if __name__ == '__main__':
    for a, b, c in pythagorean(1000):
        if a+b+c == 1000:
            print a*b*c
            break
