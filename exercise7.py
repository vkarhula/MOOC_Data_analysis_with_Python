# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:08:12 2020

@author: OMISTAJA
"""

shape = 1
while shape != ' ':
    shape = input("Which area you want to calculate?" 
                    "\nt=triangle, r=rectancle, c=circle ")
    if shape == 't':
        #print("triangle")
        a = float(input("Give base of the triangle: "))
        b = float(input("Give height of the triangle: "))
        print(f"The area is {a*b/2:.6f}")
    elif shape == 'r':
        #print("rectangle")
        a = float(input("Give width of the rectangle: "))
        b = float(input("Give height of the rectangle: "))
        print(f"The area is {a*b:.6f}")
    elif shape == 'c':
        #print("circle")
        a = float(input("Give radius of the circle: "))
        print(f"The area is {3.14159265*a**2:.6f}")
    elif shape == ' ':
        print("Goodbye")
        break
    else:
        print("Unknown area!")
        continue
    