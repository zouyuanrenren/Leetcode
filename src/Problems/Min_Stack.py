'''
Created on 2 Jan 2015

@author: Yuan
'''
class MinStack:
    
    def __init__(self):
        self.stack = list()
        self.min_stack = list()
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        return x

    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    # @return an integer
    def getMin(self):
        if len(self.stack) > 0:
            return self.min_stack[-1]
        else:
            return None
 
ms = MinStack()
ms.push(-3)
print ms.getMin()
ms.pop()
print ms.getMin()