# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 18:22:08 2019

@author: stali
"""
"""
Write a program to calculate the credit card balance after one year if a person
only pays the minimum monthly payment required by the credit card company each month.
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total_paid = 0

for i in range(0, 12):
    # Calculating payment for each month and reducing the balance
    payment = monthlyPaymentRate * balance
    #total_paid += payment
    balance -= payment
    
    #Adding Interest to the balance
    balance = balance + (annualInterestRate / 12) * balance
    #print('The remaining balance for month {} is {:.2f}'.format(i+1 ,balance))

print('Remaining balance: {:.2f}'.format(balance)) 