'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) == 0:
            return 0
        current = 0
        maxdis = 0
        nextmax = 0
        step = 0
        while nextmax < len(A)-1:
            if current <= maxdis:
                nextmax = max(nextmax, current+A[current])
                current += 1
            else:
                step += 1
                maxdis = nextmax
        if len(A) == 1:
            return 0
        return step+1       
    
print Solution().jump([2,3,1,1,4])