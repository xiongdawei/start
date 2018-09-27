a=[1,2,4,5,6,3,4,100,-100]
b=[]
while(len(a)!=0):
    min=a[0]
    for i in range(len(a)):
        if(a[i]<min):
            min=a[i]
    b.append(min)
    a.remove(min)
    print(a,b)
