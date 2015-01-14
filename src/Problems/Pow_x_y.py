'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
Pow(x,n) is inductively defined as follows:
    = 1 if n = 0
    = 1/Pow(x,-n) if n < 0
    = Pow(x*x, n/2) if n is even
    = Pow(x*x, n/2)*x if n is odd

Note that in the n < 0 case, the result needs to be a float number
'''
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        return 1 if n == 0 else float(1)/self.pow(x, -n) if n < 0 else self.pow(x*x, n/2)*x if n %2 else self.pow(x * x, n/2)
    

print Solution().pow(5, -4)