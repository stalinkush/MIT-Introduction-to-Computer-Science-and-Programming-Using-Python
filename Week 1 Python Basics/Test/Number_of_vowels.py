# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:01:51 2019

@author: stali
"""

"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

def num_vows(s):
    """
    This function takes in an string and 
    returns a tuple consisting of 
    (Num of Vowels, Num of Non Vowels)
    """
    s = s.lower()
    vow, non = 0, 0
    
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' \
        or i == 'u':
            vow += 1
        else:
            non += 1
    
    print(' The Number of Vowels: {}\n The Number of Non Vowels: {}'\
          .format(vow, non))
    
    return (vow, non) 