#Author Name - Aryan Sahni
#Date -05/12/2023
#file - stack.py
#Description - calculator that will convert a command from infix to postfix

class Stack:
    
    def __init__(self):
        self.stack=[]
     

    def isEmpty(self):
        return self.stack == []
        
    def push(self, item):
        self.stack.append(item)
    

    def pop(self):
        outcome = -1
        if self.stack != []:
            outcome = self.stack.pop()
        return outcome
        
    
    def peek(self):
        for i in range (len(self.stack)):
            return self.stack[len(self.stack)-1]


        

    def size(self):
        return len(self.stack)
     

# a driver program for class Stack

if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    
    assert s.size() == 0
    assert s.peek() == None

