#!/usr/bin/env python

from time import time

REPS = 17500


def insert():
    m = []
    now = time()
    i = 0
    while i < 17500:
        m.insert(0, i)
        i += 1
        print('Elapsed (insert):', time() - now)


def colonZero():
    m = []
    i = 0
    now = time()
    while i < REPS:
        m[:0] = [i]
        i += 1
        print('Elapsed (colon-0):', time() - now)


def main():
    insert()
    colonZero()


if __name__ == '__main__':
    main()
    input('>')
