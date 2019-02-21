# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 22:38:36 2019

@author: stali
"""

def gcditer(a,b):
    """
    This fuction takes in two intergers and 
    returns gcd of the numbers
    """
    x = min(a, b)
    while x != 0:
        if a%x == 0 and b%x == 0:
            return x
        x -= 1
    return 1