'''
Created on 5 Jan 2015

@author: Yuan
'''

'''
This problem can be solved with greedy strategy.
1. the initial maximal reachable position is 0
2. the initial position is 0
3. for each reachable position i, the maximal reachable position = max(currentmax, i+A[i])
'''


class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        Max = 0
        index = 0
        while index <= Max and index < len(A):
            Max = max(A[index]+index, Max)
            index += 1
        return Max >= len(A) -1