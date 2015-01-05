'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
easiest solution is to use a dic to maintain the count of all elements.
Whenever a count exceeds the majority, return the element
'''
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dict = {}
        for n in num:
            dict[n] = 1 if n not in dict else dict[n] + 1
            if dict[n] > len(num) / 2:
                return n
        return 0