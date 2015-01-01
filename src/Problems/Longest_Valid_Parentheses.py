'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if len(s) < 2:
            return 0
        l = 0
        current = 0
        stack = []
        for ch in s:
            if ch == "(":
                if current > 0:
                    stack.append(current)
                    l = max(l, current)
                    current = 0
                stack.append(ch)
            else:
                if stack and stack.pop() == "(":
                    current += 2
                    while stack and stack[-1] != "(":
                        current += stack.pop()
                else:
                    l = max(l, current)
                    current = 0
        return max(l, current)
                


print Solution().longestValidParentheses(")(((((()())()()))()(()))(")        