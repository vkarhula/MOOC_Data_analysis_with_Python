# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:47:00 2020

@author: OMISTAJA
"""


#help(print)

def sum_of_squares(a,b):
    "Computes the sum of argumets squared"
    return a**2 + b**2
print(sum_of_squares(3,4))

# Exercise 6
def triple(a):
    return a*3

def square(b):
    return b**2

#print(f"triple({5}) == {triple(5)}")
#print(f"square({5}) == {square(5)}")

for i in range(1,11):
    #print(i)
    if square(i) <= triple(i):
        print(f"triple({i}) == {triple(i)} ", end="")
        print(f"square({i}) == {square(i)}")
    else:
        break
    
    
    