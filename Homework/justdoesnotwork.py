# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:13:40 2018

@author: 28773
"""
def redcheck(sec,g1,g2,k1,k2):
    total=0
    for i in range(g1,g2):
        for j in range(k1,k2):
            if(sec[i][j][2]>120 and sec[i][j][1]<80 and sec[i][j][0]<80):
                total=total+1
    return total
def yellowcheck(sec,g1,g2,k1,k2):
    total=0
    for i in range(g1,g2):
        for j in range(k1,k2):
            if(sec[i][j][2]<80 and sec[i][j][1]>160 and sec[i][j][0]>160):
                total=total+1
    return total
def greencheck(sec,g1,g2,k1,k2):
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
print(origin[500][500])
origin[500][500][0]=100
print(origin[500][500][0],origin[500][500][1],origin[500][500][2])
print(checkcolor(origin,0,1000,0,333))
