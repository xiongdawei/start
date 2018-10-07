# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:05:13 2018

@author: 28773
"""
import matplotlib as mtp
import numpy as np
import time
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
                print('i',blist)
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
