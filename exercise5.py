# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:17:14 2020

Exercise 5 (two dice)
Let us consider throwing two dice. (A dice can give a value between 1 and 6.) Use two nested for loops 
in the main function to iterate through all possible combinations the pair of dice can give. 
There are 36 possible combinations. Print all those combinations as (ordered) pairs that sum to 5. 
For example, your printout should include the pair (2,3). Print one pair per line.

@author: OMISTAJA
"""



for i in range(1,7):
    for j in range(1,7):
        if i+j == 5:
            #print("(",i,",",j,")")
            #print("({0},{1})".format(i,j))
            print(f"({i:1d},{j:1d})")
            
