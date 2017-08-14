#!/usr/bin/env python
# coding=utf-8

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Check v1.0'
print 'Testees  must be at least 2 chars long.'
myInput = raw_input('Identifier to test?\n')

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''invalid: first symbol must be
                alphabetic'''
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print '''invalid: remaining
                                sysmbols must be alphanumeric'''
                break
            else:
                print "okay as an identifier"
