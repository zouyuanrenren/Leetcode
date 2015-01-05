'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
every 5 numbers less than n add 1 trailing 0, total is n/5
every 25 numbers less than n add another trailing 0, total is n/5/5
every 125 numbers less than n add another trailing 0, total is n/5/5/5
so on and on...
We only need to compute such numbers.
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