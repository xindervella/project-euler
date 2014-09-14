#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import count
from factors import uniprimefactors


def triangle():
    for i in count(2):
        yield i * (i+1) / 2

if __name__ == '__main__':
    for trin in triangle():
        #if len(list(factors(i))) > 500:
        #    print i
        #    break
        if reduce(lambda x,y:x*y, [i+1 for i in uniprimefactors(trin).values()]) > 500:
            print trin
            break
