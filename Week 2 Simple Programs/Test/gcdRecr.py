# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 02:13:20 2019

@author: stali
"""

def gcdRecr(a, b):
    """
    This function takes two numbers and 
    returns gcd of the numbers
    """
    if b == 0:
        return a
    else:
        return gcdRecr(b, a%b) 