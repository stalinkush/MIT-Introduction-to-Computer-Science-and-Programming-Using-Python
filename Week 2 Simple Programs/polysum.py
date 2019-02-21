# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 02:29:45 2019

@author: stali
"""

def polysum(n, s):
    """
    This function takes two arguments
    n: no of sides of polygon
    s: length of each side
    
    returns: 
        sum of area and square of permiter of polygon
    """
    
    from math import tan, pi
    #Calculating area and perimeter of polygon
    area = (0.25*n)*s**2 / tan(pi/n)
    perimeter = n*s
    
    return round(area + perimeter**2, 4)