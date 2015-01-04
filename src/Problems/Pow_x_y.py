'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return float(1)/self.pow(x, -n)
        return self.pow(x * x, n/2)*x if n%2 else self.pow(x * x, n/2)
    

print Solution().pow(5, -4)