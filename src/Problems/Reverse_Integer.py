'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
Relative simply problem.
Need to consider a few corner cases:
1. x is negative.
2. x is > 2^31-1.
'''
class Solution:
    # @return an integer
    def reverse(self, x):
        result = 0
        num = abs(x)
        while num:
            result = result * 10 + num % 10
            num /= 10
        return 0 if result > 2**31-1 else result if x >= 0 else -result

print Solution().reverse(1234567802)