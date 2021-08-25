# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:52:00 2020

Exercise 11 (interleave)
Write function interleave that gets arbitrary number of lists as parameters. You may assume that 
all the lists have equal length. The function should return one list containing all the elements 
from the input lists interleaved. Test your function from the main function of the program.

Example: interleave([1,2,3], [20,30,40], ['a', 'b', 'c']) should return [1, 20, 'a', 2, 30, 'b', 3, 40, 'c']. 
Use the zip function to implement interleave. Remember the extend method of list objects.

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
