# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:17:14 2020

@author: OMISTAJA
"""


for i in range(1,7):
    for j in range(1,7):
        if i+j == 5:
            #print("(",i,",",j,")")
            #print("({0},{1})".format(i,j))
            print(f"({i:1d},{j:1d})")
            