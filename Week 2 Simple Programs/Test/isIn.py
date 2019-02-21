# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 02:17:50 2019

@author: stali
"""


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string 
   
    returns: True if char is in aStr; False otherwise
    '''
    # Base case: If aStr is empty, we did not find the char.
    if aStr == '':
        return False

    # Base case: if aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
        return char == aStr

    # Base case: See if the character in the middle of aStr equals the 
    #   test character 
    middle = len(aStr) // 2
    if aStr[middle] == char:
        return True
      # We found the character!

   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
    elif aStr[middle] > char:
        return isIn(char, aStr[:middle])
   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
    else:
        return isIn(char, aStr[middle+1:]) 