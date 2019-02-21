# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:47:32 2019

@author: stali
"""

balance = 4773
new_bal = 0
annualInterestRate = 0.2
monthly_payment = 10

while True:
    new_bal = balance
    for i in range(0,12):
        new_bal -= monthly_payment
        
        new_bal = new_bal + (annualInterestRate / 12) * new_bal
    
    #print('Balance is {:.4f}'.format(new_bal))
    monthly_payment += 10
    
    if new_bal < 0:
        break
    
print('Lowest Payment: {}'.format(monthly_payment-10)) 