#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations_with_replacement


def ispalindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) / 2))


if __name__ == '__main__':
    print max([i * j
               for i, j in combinations_with_replacement(range(900, 999), 2)
               if ispalindromic(str(i * j))])
