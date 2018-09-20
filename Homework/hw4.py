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
    
import turtle as tl 

def draw_smalltree(tree_length,tree_angle):
    '''
    绘制分形树函数
    '''
    if tree_length >= 3:
        tl.forward(tree_length)
        tl.right(tree_angle) 
        draw_smalltree(tree_length - 10,tree_angle)

        tl.left(2 * tree_angle) 
        draw_smalltree(tree_length -10,tree_angle)

        tl.right(tree_angle) #???
        tl.backward(tree_length)

def main():
    tl.penup()
    tl.left(90) 
    #tl.backward(250)
    tl.bgcolor("light blue")
    tl.pendown()
    tree_length = 60 
    tree_angle = 20 
    draw_smalltree(tree_length,tree_angle)
main()
#fib(40)
a=[0,1,1]
r=0
for i in range(1,102):
    a[i%3]=a[(i+1)%3]+a[(i+2)%3]
    print(a[i%3])
    r=r+a[i%3]
print(r) 