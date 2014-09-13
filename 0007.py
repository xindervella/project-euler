#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lazy import lazylist


@lazylist
def prime():

    def hexstep():
        """Generate 6n-1, 6n+1 sequence"""
        n = 1
        while True:
            hex = 6 * n
            yield hex - 1
            yield hex + 1
            n += 1

    def isprime(n):
        for p in primes:
            if n % p == 0:
                return False
            if p ** 2 > n:
                return True

    yield 2
    yield 3
    primes = [2, 3]

    for n in hexstep():
        if isprime(n):
            yield n
            primes.append(n)


if __name__ == '__main__':
    print prime()[10000]
