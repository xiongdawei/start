# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 09:33:57 2018

@author: 28773
"""
a=eval(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(str(j)+"*"+str(i)+"="+str(i*j), end=' ')
    print()
i=1
while i<=a:
    j=1
    while j<=i:
        print(str(j)+"*"+str(i)+"="+str(i*j), end=' ')
        j=j+1
    print()
    i=i+1