# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:23:39 2018

@author: 28773
"""

def grid(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score >=60:
        return 'C'
    else:
        return 'D'
class student():
    """
    Class of a student that includes name, age, gender, and scores of all subjects
    """
    def __init__(self,getname='AMD',getage=100,getgender='Male',getgrades={'Math':100, 'CS':0,'Man':80,"Eng":88}):
        self.name=getname
        self.age=getage
        self.gender=getgender
        self.grades=getgrades
    def setname(self,name):
        self.name=name
    def setage(self,age):
        self.age=age
    def setgender(self,gender):
        self.gender=gender
    def setgrade(self,subject,grade):
        self.grades[subject]=grade
    def setgrades(self,gradelist):
        num=0
        for i in self.grades:
            self.grades[i]=gradelist[num]
            num+=1
    def printname(self):
        return self.name
    def printage(self):
        return self.age
    def printgender(self):
        return self.gender
    def printgrades(self):
        return self.grades
    def avggrades(self):
        avg=0
        for i in self.grades:
            avg=avg+self.grades[i]
        avg=avg/len(self.grades)
        return avg
    def checkgrade(self,subject):
        return grid(self.grades[subject])
    def __str__(self):
        out=''
        out=out+"Student name: "+self.name+'\n'
        out=out+"Student gender: "+self.gender+'\n'
        out=out+"Student age: "+str(self.age)+'\n'
        out=out+"Student scores: "+'\n'
        for i in self.grades:
            out=out+"subject: "+i+"  score: "+str(self.grades[i])+'\n'
        return out
    def avggrid(self):
        return grid(self.avggrades())
class ibstudent(student):
    def __init__(self,initia,initee):
        student.__init__(self)
        self.ia=initia
        self.ee=initee
    def setee(self,getee):
        self.ee=getee
    def printee(self):
        return self.ee
    def setia(self,getia):
        self.ia=getia
    def printia(self):
        return self.ia
scoredict={'Math':100, 'CS':0,'Man':80,"Eng":88}
JSH=student('Huang',50,'Male',scoredict)
print(JSH.avggrades(),JSH.avggrid())
JSH.setname("AMD")
print(JSH.printname())
JSH.setgender("Alien")
print(JSH.printgender())
JSH.setgrade('Eco',90)
JSH.printgrades()
print('Math: '+JSH.checkgrade('Math'))
print(JSH)
print(JSH.avggrades(),JSH.avggrid())
R=ibstudent(90,80)
R.setee(100)
print(R.printee(),R.printia(),R.avggrades())