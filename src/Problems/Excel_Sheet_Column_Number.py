'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
excel sheet column number examples:
1    A
2    B
...
26    Z
27    AA


This is apparently a sequence of number with radix 26. While instead of 0-25, the digit value is 1-26.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        num = 0
        for c in s:
            num *= 26
            num += ord(c)-ord("A") +1
        return num
    
print Solution().titleToNumber("BBA")