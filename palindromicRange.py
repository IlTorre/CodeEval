#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Marco Torreggiani'

import sys


if __name__=='__main__':

    fil = open(sys.argv[1], 'r')
    for row in fil.readlines():
        L,R=row.split(' ')
        L=int(L)
        R=int(R)
        pal=[]
        int=[]
        for i in xrange(L,R+1):
            x=str(i)
            if x==x[::-1]:
                pal.append(x)

        print