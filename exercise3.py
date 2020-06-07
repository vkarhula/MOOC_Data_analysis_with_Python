# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:56:52 2020

@author: OMISTAJA
"""


for i in range(11):
    print(4, "multiplied by", i, "is", 4*i)

i=3
type(i)
print(type(i))

i="teksti"
print(type(i))

   
s="""A string
spanning over
several lines""" 
print(s)

print(f"{4:3d}")
print(f"{14:3d}")

print('{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))

print(3//4, 3/4, 3**4)