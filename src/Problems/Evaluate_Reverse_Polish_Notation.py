'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop()+stack.pop())
            elif ch == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2-op1)
            elif ch == "*":
                stack.append(stack.pop()*stack.pop())
            elif ch == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(float(op2)/op1))
            else:
                stack.append(int(ch))
        return stack.pop()
    

print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])