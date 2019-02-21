# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:43:20 2019

@author: stali
"""

def balance_left(balance, annualInterestRate, monthly_payment):
    for i in range(0, 12):
        # Calculating payment for each month and reducing the balance
        balance -= monthly_payment
        #total_paid += payment
    
        #Adding Interest to the balance
        balance = balance + (annualInterestRate / 12) * balance
    return balance


def find_payment(balance, annualInterestRate):
    low = balance / 12
    high = balance / 2
    
    while True:
        payment = (low+high) / 2
        remaining = balance_left(balance, annualInterestRate, monthly_payment=payment)
        balx = remaining - balance
        
        if abs(balance + balx) <= 0.01:
            break
        
        if remaining > 0:
           low = payment
        else:
            high = payment
    
    return payment  
        