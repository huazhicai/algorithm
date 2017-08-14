#!/usr/bin/env python
# coding=utf-8
import string
import keyword

alphas = string.letters + '_'
nums = string.digits
aplpnums = alphas = nums

print 'Testees must be at least 1 char long.'
myInput = raw_input('Identifier to test?')

if len(myInput) >= 1:
    if myInput[0] not in alphas:
        print 'invalid: first symbol must be alphabetic'
    else:
        for otherchar in myInput[1:]:
            if otherchar not in aplpnums:
                print 'invalid: remaining symbols must be alphanumeric'
                break
        else:
            if myInput in keyword.kwlist:
                print 'invalid: symbol is reserved as keyword'
            else:
                print 'okay as an identifier'
