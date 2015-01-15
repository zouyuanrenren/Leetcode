'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
Relative simply problem.
Only need to be careful about the negative numbers.
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