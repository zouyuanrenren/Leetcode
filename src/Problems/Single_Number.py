'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
We consider two possible solutions to this problem.
1. One is to use a hashmap, to maintian the count of each number.
    if a number has count 1, it is the single number.
2. The other is to use bit manipulation.
    we get the exclusive or (^) of all numbers. 
    If the numbers are pairwise, final results should be 0, with the additional single number, the results is the single number. 

The following shows the bit manipulation solution.
'''
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = A[0]
        for i in range(1,len(A)):
            result = result ^ A[i]
        return result
        