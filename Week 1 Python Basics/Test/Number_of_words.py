# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:21:26 2019

@author: stali
"""
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'

index = 0
count = 0

for i in s:
    if i == 'b':
        if s[index:index+3] == 'bob':
            count += 1
    index += 1

print('Number of times bob occurs is: {}'.format(count)) 