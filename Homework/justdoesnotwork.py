# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:13:40 2018

@author: 28773
"""
def redcheck(sec,g1,g2,k1,k2):#check for the number of red pixels
    total=0
    for i in range(g1,g2):
        for j in range(k1,k2):
            if(sec[i][j][2]>120 and sec[i][j][1]<80 and sec[i][j][0]<80):
                total=total+1
    return total
def yellowcheck(sec,g1,g2,k1,k2):#check for the number of yellow pixels
    total=0
    for i in range(g1,g2):
        for j in range(k1,k2):
            if(sec[i][j][2]<80 and sec[i][j][1]>160 and sec[i][j][0]>160):
                total=total+1
    return total
def greencheck(sec,g1,g2,k1,k2):#check for the number of green pixels
    total=0
    for i in range(g1,g2):
        for j in range(k1,k2):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            if(sec[i][j][1]>120 and sec[i][j][2]<80):
                total=total+1
    return total
def checkcolor(sec,g1,g2,k1,k2):
    red=redcheck(sec,g1,g2,k1,k2)
    yellow=yellowcheck(sec,g1,g2,k1,k2)
    green=greencheck(sec,g1,g2,k1,k2)
    print(red,yellow,green)
    if(max(red,yellow,green))==red:
        return 'red'
    elif(max(red,yellow,green))==green:
        return 'green'
    else:
        return 'yellow'
def gradient(sec):
    gre=[]
    red=[]
    yel=[]
    for i in range(1000):
        cur1=0
        cur2=0
        cur3=0
        for j in range(1000):
            if(sec[i][j][2]>120 and sec[i][j][1]<80 and sec[i][j][0]<80):
                cur3+=1
            if(sec[i][j][1]>120 and sec[i][j][2]<80):
                cur2+=1
            if(sec[i][j][2]<80 and sec[i][j][1]>160 and sec[i][j][0]>160):
                cur1+=1
        red.append(cur3)
        gre.append(cur2)
        yel.append(cur1)
    return red,gre,yel
import cv2
import numpy as np
origin=cv2.resize(cv2.imread('E:\\cvpic\\JP.jpg'),(1000,1000))#cv2.cvtColor(,cv2.COLOR_BGR2RGB)
cv2.imwrite("E:\\cvpic\\HLD.jpg",origin)
kernel = np.array([[0,0,1,0,0],
                   [0,1,1,1,0],
                   [1,1,1,1,1],
                   [0,1,1,1,0],
                   [0,0,1,0,0]])/13
#origin=cv2.filter2D(origin,-1,kernel)
cv2.imwrite("E:\\cvpic\\HLD2.jpg",origin)
a,b,c=gradient(origin)
numbers=int(input("please input the number of traffic lamps in the frame"))
seg=int(1000/numbers)
start=0
print("method 1")
for i in range(numbers):
    print(checkcolor(origin,0,1000,start,start+seg))
    start=start+seg
print("method 2")
for i in range(10,1000):
    if a[i]-a[i-10]>30 and a[i]-a[i+10]>30:
        print('red')
        i=i+50
    elif b[i]-b[i-10]>30 and b[i]-b[i+10]>30:
        print('green')
        i=i+50
    elif c[i]-c[i-10]>30 and c[i]-c[i+10]>30:
        print('yellow')
        i=i+50