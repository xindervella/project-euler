#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {1: 1}


def collatz_seq(n):
    return d[n] if n in d else d.setdefault(n,
            1 + (collatz_seq(3*n+1) if n%2 else collatz_seq(n/2)))

if __name__ == '__main__':
    print max((collatz_seq(i), i) for i in range(2, 10**6))
