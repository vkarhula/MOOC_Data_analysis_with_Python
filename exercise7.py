# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:08:12 2020

@author: OMISTAJA
"""

# Exercise 7 (areas of shapes)
# Create a program that can compute the areas of three shapes, triangles, rectangles and circles, when their dimensions are given.

# An endless loop should ask for which shape you want the area be calculated. An empty string as input will exit the loop. 
# If the user gives a string that is none of the given shapes, the message “unknown shape!” should be printed. 
# Then it will ask for dimensions for that particular shape. When all the necessary dimensions are given, it prints the area, 
# and starts the loop all over again. Use format specifier f for the area.

# What happens if you give incorrect dimensions, like giving string “aa” as radius? You don’t have to check for errors in the input.

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
    
