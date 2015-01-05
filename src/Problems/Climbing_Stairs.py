'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
A typical Fibonacci number problem. Use dynamic programming
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        pre1 = 1
        pre2 = 1
        for i in range(2,n+1):
            current = pre1+pre2
            pre2 = pre1
            pre1 = current
        return current
        