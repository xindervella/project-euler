#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import takewhile


def fib():
    a, b = 1, 0
    while True:
        yield b
        a, b = a+b, a

if __name__ == '__main__':
    print sum([i for i in takewhile(lambda x: x < 4*10**6, fib()) if i % 2 == 0])
