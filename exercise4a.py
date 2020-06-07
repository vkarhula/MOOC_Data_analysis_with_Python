# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:16:03 2020

@author: OMISTAJA
"""

#kokeiluja

for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j:4d}", end='')
    print("\n")
    
for i in range(1,7):
    for j in range(1,7):
        if i+j == 5:
            print(f"({i},{j})")
            print("({0},{1})".format(i,j))
            
def sum_of_squares(lst):
    "Computes the sum of squares of elements in the list given as parameter"
    s=0
    for x in lst:
        s += x**2
    return s
print(sum_of_squares([-2]))
print(sum_of_squares([-2,4,5]))

def sum_of_squares2(*t):
    "Computes the sum of squares of arbitrary number of arguments"
    s=0
    for x in t:
        s += x**2
    return s
print(sum_of_squares2(-2))
print(sum_of_squares2(-2,4,5))

lst=[1,5,8]
print("With list unpacked as arguments to the functions:", sum_of_squares2(*lst))
print(sum_of_squares(lst))    # Does not work correctly

def oma_funktio(a):
    "Virpin oma funktio, parametrina neliön sivun pituus"
    return a**2
a=5
print("Arvon {} neliö on {}".format(a, oma_funktio(a)))
print(f"Arvon {a} neliö on {oma_funktio(a)}")
#help(oma_funktio)

def doubleStuff(aList):
    """ Overwrite each element in aList with double its value. """
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]

things = [2, 5, 9]
print(things)
doubleStuff(things)
print(things)