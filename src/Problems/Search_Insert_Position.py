'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
This problems essentially asks for the position of the first element that is larger or equal to the target.
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        for index, item in enumerate(A):
            if item >= target:
                return index
        return len(A)
        