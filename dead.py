# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:14:52 2018

@author: 28773
"""
import urllib.request
a=open("test.txt","r")
b=open("output.txt","w")
#q1
rev=[]
while True:
    if(len(a.readline())==0):
        break
    else:
        rev.append(a.readline())
for i in rev:
    b.write(str(i)+"\n")
#q2
snk=[]
c=a.readlines()
for i in c:
    if "snake" in i:
        snk.append(i)
for i in snk:
    b.write(str(i)+"\n")
#q3
num=[]
while True:
    if(len(a.readline())==0):
        break
    else:
        num.append(a.readline())
for i in range(len(num)):
    if(i>9):
        b.write("0000"+str(i+1)+" "+num[i]+"\n")
    elif(i>99):
        b.write("000"+str(i+1)+" "+num[i]+"\n")
    elif(i>999):
        b.write("00"+str(i+1)+" "+num[i]+"\n")
    elif(i>9999):
        b.write("0"+str(i+1)+" "+num[i]+"\n")
    else:
        b.write(str(i+1)+" "+num[i]+"\n")
#q4
antinum=[]
while True:
     if(len(a.readline())==0):
        break
     else:
        antinum.append(a.readline())
for i in antinum:
    b.write(i[5:]+"\n")
a.close()
b.close()
        