class stack():
    def __init__(self):
        self.stack1=[]
    def isempty(self):
        if len(self.stack1)==0:
            return True
        else:
            return len(self.stack1)
    def push(self,a):
        self.stack1.append(a)
    def pop(self):
        self.stack1.remove(self.stack1[0])
    def read(self):
        return self.stack1


test=stack()
test.push(1)
test.push(2)
test.pop()
print(test.read())
print(test.isempty())
test.pop()
print(test.isempty())