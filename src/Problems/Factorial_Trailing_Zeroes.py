'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        num = 0
        while n >= 5:
            num += n/5
            n = n/5
        return num
    
sol = Solution()
for i in range(100):
    print i, sol.trailingZeroes(i)