'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if len(A) == 0:
            return 1
        A.sort()
        result = -1
        pos = False
        if A[0] > 0:
            pos = True
            if A[0] > 1:
                return 1
        for i in range(1, len(A)):
            if A[i] > 0:
                if pos:
                    if A[i] > A[i-1]+1:
                        result = A[i-1]+1
                        break
                else:
                    pos = True
                    if A[i]>1:
                        result = 1
                        break
        if pos:
            if result == -1:
                return A[len(A)-1]+1
            else:
                return result
        else:
            return 1
        
print Solution().firstMissingPositive([-2,5])