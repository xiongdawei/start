# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 06:06:15 2018

@author: 28773
"""

#q1
for i in range(12):
    mp=balance*annualInterestRate
    up=balance-mp
    interest=(annualInterestRate/12)*balance
    balance=balance+interest
print("Remaining balance:%.2f"%balance)
#q2
fp=0
while True:
    b=balance
    a=annualInterestRate
    for i in range(12):
        mi=annualInterestRate/12
        b=b-fp
        b=b+mi*b
    if(b==180):
        break
    fp=fp+10
print("Lowest Payment: "+str(fp))
#q3
mi=annualInterestRate/12
fp=0
lb=balance/12
ub=(balance*((1+mi)**12))/12
while True:
    b=balance
    a=annualInterestRate
    for i in range(12):
        mi=annualInterestRate/12
        b=b-fp
        b=b+mi*b
    if(b-180<=0.0000001):
        break
    else:
        if(b>180):
            lb=(lb+ub)/2
            mi=(lb+ub)/2
        else:
            ub=(lb+ub)/2
            mi=(lb+ub)/2
print("Lowest Payment: "+str(fp))
        
