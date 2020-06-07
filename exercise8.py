# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:41:30 2020

@author: OMISTAJA
"""

import math

#def solve_quadratic(*lst):
#    print(f"{lst}")
    
#lst = [1,-3,2]
#solve_quadratic(*lst)

def solve_quadratic(*lst):
    #print(f"{lst}")
    a = float(lst[0])
    b = float(lst[1])
    c = float(lst[2])
    #print("{} {} {}".format(a,b,c))
    x1 = (-b + math.sqrt(b*b -4*a*c))/2*a
    x2 = (-b - math.sqrt(b*b -4*a*c))/2*a
    #print(f"({x1:.1f},{x2:.1f})")
    #x = (f"({x1:.1f},{x2:.1f})")
    #x = [x1, x2]
    x = (x1,x2)
    return x
    
#lst = [1,-3,2]
print(solve_quadratic(1,-3,2))
print(solve_quadratic(1,2,1))
