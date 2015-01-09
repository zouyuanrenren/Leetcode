'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
As the name suggests this problem can be solved with stacks.
There are several things need to be maintained:
1. the value of elements;
2. the corresponding minimal values of elements in stack;
    when the value stack is popped, the current minimal value needs to be updated as the popped value might be smaller than any remaining one.
    this can be achieved by:
        a. maintaining a minimum stack. 
           When a new element is pushed into/popped from the value stack, 
           it will be pushed into/popped from the minimum stack if its value is no higher than existing minimums.
           e.g. [1,3,4,6,4] will have a minimum stack [1]
           This may cost extra space when there are multiple minimums with equal values, 
           e.g. [1,1,1,1,1,1,1] will have a minimum stack [1,1,1,1,1,1,1]
        b. maintaining a minimum stack and minimum count stack.
           Different from the above approach, the minimum stack only maintain unique values
           and a separate minimum count stack maintains the count of each minimum.
           e.g. [1,1,1,1,1,1,1] will have a minimum stack [1] and a count stack[7]
           When a element is popped and it is equal to the minimum, 
           then the minimum count will be decreased by 1 and be popped when the count reaches 0.
           This may cost extra space when there are multiple descending unique minimums.
           For example, [5,4,3,2,1] will have a minimum stack [5,4,3,2,1] and a count stack [1,1,1,1,1]
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