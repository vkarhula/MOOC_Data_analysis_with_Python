# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:47:00 2020

Exercise 6 (triple square)
Write two functions: triple and square. Function triple multiplies its parameter by three. 
Function square raises its parameter to the power of two. For example, we have equalities triple(5)==15 and square(5)==25.

Part 1.
In the main function write a for loop that iterates through values 1 to 10, and for each value prints its triple and its square. 
The output should be as follows:
triple(1)==3 square(1)==1
triple(2)==6 square(2)==4

Part 2.
Now modify this for loop so that it stops iteration when the square of a value is larger than the triple of the value, 
without printing anything in the last iteration.

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
    
    
    
