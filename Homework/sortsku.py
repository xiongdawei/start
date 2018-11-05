# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:05:13 2018

@author: 28773
"""
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
def quicksort(alist):
    sort(alist,0,len(alist)-1)
def sort(alist,start,end):
    if start<end:
        mid=partitionsort(alist,start,end)
        sort(alist,start,mid-1)
        sort(alist,mid+1,end)
def partitionsort(alist,start,end):
    pivot=alist[start]
    left=start+1
    right=end
    while True:
        while left<=right and alist[left]<pivot:
            left+=1
        while left<=right and alist[right]>pivot:
            right-=1
        if right<left:
            break
        else:
            alist[left],alist[right]=alist[right],alist[left]
    alist[start],alist[right]=alist[right],alist[start]
    return right
