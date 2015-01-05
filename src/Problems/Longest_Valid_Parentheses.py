'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
A typical dynamic programming problem.
Can also be solved with a stack.
Solution uses a cache
Solution2 uses DP
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
    
class Solution2:
    def longestValidParentheses(self, s):
        if s == None or len(s) < 2:
            return 0
        dp = [0,0]
        Max = 0
        for i in range(1,len(s)):
            c = s[i]
            num = 0
            if c == ")":
                if s[i-1] == "(":
                    num = max(num, dp[-2]+2)
                else:
                    last = dp[-1]
                    if i-last-1 >= 0 and s[i-last-1] == "(":
                        new = dp[-1]+2
                        num = max(num, new+dp[-new])
            dp.append(num)
            Max = max(Max, num)
        return Max


print Solution2().longestValidParentheses(")(((((()())()()))()(()))(")        