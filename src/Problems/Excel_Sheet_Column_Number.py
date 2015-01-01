'''
Created on 1 Jan 2015

@author: Yuan
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
    
print Solution().titleToNumber("BA")