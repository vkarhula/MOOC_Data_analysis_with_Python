# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:52:00 2020

@author: OMISTAJA
"""


def interleave(L1,L2,L3):
    L = []
    for a,b,c in zip(L1,L2,L3):
        L.append(a)
        L.append(b)
        L.append(c)
    return L
    #return list(zip(L1,L2,L3))


def interleave_extend(L1,L2,L3):
    L = []
    for a,b,c in zip(L1,L2,L3):
        L.extend([a,b,c])
    return L

print(interleave([1,2,3], [20,30,40], ['a', 'b', 'c']))
print(interleave_extend([1,2,3], [20,30,40], ['a', 'b', 'c']))