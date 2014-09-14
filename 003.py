#!/usr/bin/env python
# -*- coding: utf-8 -*-


def prime_factors(n):
    f = 2
    while f ** 2 <= n:
        while not n % f:
            yield f
            n /= f
        f += 1
    if n > 1:
        yield n

if __name__ == '__main__':
    print max(prime_factors(600851475143))
