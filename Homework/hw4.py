# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:56:07 2018

@author: 28773
"""

def fibsum(a):
    '''
    input the length of fibonacci sequence and outputs the sum
    '''
    r=0
    for i in range(a):
        r=r+fib(i)
    return r
def fib(a):
    '''
    input the nth term of  fibonacci sequence and outputs the term
    '''
    if(a==0 or a==1):
        return(1)
    else:
        return(fib(a-1)+fib(a-2))
def sumd(a,b):
    '''
    input the start and end and outputs the sum of terms within
    '''
    if(a==b):
        return a
    else:
        return a+sumd(a-1,b)
def power(a,b):
    '''
    returns a**b
    '''
    if(b==1):
        return a
    else:
        return(a*power(a,b-1))
def jiecheng(a):
    '''
    returns a!
    '''
    if(a==1):
        return 1
    else:
        return a*jiecheng(a-1)