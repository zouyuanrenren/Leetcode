'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
Basic stack problem.
Idea is, going throught the input string:
    1. when encounter operator, pop the operands and push the results back
    2. when encounter operand, push it into the stack
    3. when string is empty, pop the stack to get the result
only thing that needs attention is that, some operators are not symmetric. So remember the order.
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