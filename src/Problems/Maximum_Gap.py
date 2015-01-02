'''
Created on 2 Jan 2015

@author: Yuan
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        # should use radix sort!
        num.sort()
        gap = 0
        for i in range(1, len(num)):
            gap = max(gap, num[i] - num[i+1])
        return gap
    