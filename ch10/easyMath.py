#!/usr/bin/env python
from operator import add, sub, mul, truediv
from random import randint, choice

ops = {'+': add, '-': sub, '*': mul, '/': truediv}
MAXTRIES = 2


def doprob():
    op = choice('+-*/')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0], op, nums[1])
    opps = 0
    while True:
        try:
            if int(input(pr)) == ans:
                print('correct')
                break
            elif opps == MAXTRIES:
                print('sorry... the answer is\n%s%d' % (pr, ans))
            else:
                print('incorrect... try again')
                opps += 1
        except (KeyboardInterrupt, EOFError, ValueError) as err:
            print(str(err))
            print('invalid input ... try again')


def main():
    while True:
        doprob()
        try:
            opt = input('Again? [y/n]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()
