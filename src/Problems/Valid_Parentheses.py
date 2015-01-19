'''
Created on 19 Jan 2015

@author: Yuan
'''
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif c == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif c == "}":
                if not stack or stack.pop() != "{":
                    return False
            else:
                stack.append(c)
        return not stack
        
print Solution().isValid("((())[]{}{})")