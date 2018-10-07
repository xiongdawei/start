# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:05:13 2018

@author: 28773
"""
import matplotlib as plt
import numpy as np
import time
import random
def insectionsort(alist):
    '''
    takes in a list of numbers and returns the sorted list
    '''
    blist=[alist[0]]
    for i in range(1,len(alist)):
        ins=False
        for j in range(len(blist)):
            if alist[i]<blist[j]:
                blist.insert(j,alist[i])
                ins=True
                break
        if(ins==False):
            blist.append(alist[i])
    return blist
def selectionsort(alist):
    '''
    takes in a list of numbers and returns the sorted list
    '''
    blist=[]
    while(len(alist)!=0):
        low=alist[0]
        for i in range(len(alist)):
            if(alist[i]<low):
                low=alist[i]
        blist.append(low)
        alist.remove(low)
    return blist
def bubblesort(alist):
    '''
    takes in a list of numbers and returns the sorted list
    '''
    for i in range(len(alist)):
        for j in range(i):
            if alist[i]<alist[j]:
                alist[i],alist[j]=alist[j],alist[i]
    return alist
def mergesort(alist):
    '''
    takes in a list of numbers and returns the sorted list
    '''
    if len(alist)>1:
        left=mergesort(alist[:len(alist)//2])
        right=mergesort(alist[len(alist)//2:])
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k]=left[i]
                i=i+1
            else:
                alist[k]=right[j]
                j=j+1
            k=k+1
        while i < len(left):
            alist[k]=left[i]
            i=i+1
            k=k+1
        while j < len(right):
            alist[k]=right[j]
            j=j+1
            k=k+1
    return alist
x=[i for i in range(1000,10001,1000)]
y1,y2,y3,y4=[],[],[],[]
cur=[]
for i in x:
    testlist=[]
    for j in range(i):
        testlist.append(random.randint(-10000,10000))
    start=time.clock()
    cur=insectionsort(testlist)
    inse=time.clock()
    cur=selectionsort(testlist)
    sele=time.clock()
    cur= bubblesort(testlist)
    bub=time.clock()
    cur=mergesort(testlist)
    mer=time.clock()
    y1.append(inse-start)
    y2.append(sele-inse)
    y3.append(bub-sele)
    y4.append(mer-bub)
l1,=plt.plot(x,y1,label="insection")
l2,=plt.plot(x,y2,label="selection")
l3,=plt.plot(x,y3,label="bubble")
l4,=plt.plot(x,y4,label="merge")
plt.show()
 