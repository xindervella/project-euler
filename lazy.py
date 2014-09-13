#!/usr/bin/env python
# -*- coding: utf-8 -*-


class LazyException(Exception):
    pass


class LazyList(object):

    def __init__(self, g):
        self.l = []
        self.g = g

    def _extend(self, n):
        self.l.extend(self.g.next() for _ in range(n))

    def __getitem__(self, k):
        if isinstance(k, int):  # l[n]
            d = k - len(self.l)
            if d >= 0:
                self._extend(d + 1)
            return self.l[k]
        elif isinstance(k, slice):  # l[start: stop: step]
            if k.stop is None:  # l[_:] -> extend to the end
                self.l.extend(self.g)
            else:
                d = k.stop - len(self.l)
                if d >= 0:
                    self._extend(d + 1)
            return self.l[k]
        else:
            raise LazyException('Invalid index %s' % k)

    def __call__(self, k):
        return self[k]

    def __iter__(self):
        def iter():
            for i in self.l:
                yield i

            for i in self.g:
                self.l.append(i)
                yield i
        return iter()


def lazylist(g):
    return lambda: LazyList(g())
