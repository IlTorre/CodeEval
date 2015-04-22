#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Marco Torreggiani'

import sys

fil = open(sys.argv[1], 'r')
test_cases=fil.read().strip().splitlines()

for test in test_cases:
    stringa,sost = test.split(';')
    sost=sost.split(',')
    print " ----- \t\t\t\t",stringa
    for i in xrange(0,len(sost),2):
        print 'Sostituisco ',sost[i],' -> ',sost[i+1],' =\t',
        stringa=stringa.replace(sost[i],sost[i+1],1)
        print stringa
    print stringa


    10011011001 => 10100111001 [replacing 0110 with 1001] => 10100110 [replacing 1001 with 0] => 11100110 [replacing 10 with 11]. So the answer is 11100110