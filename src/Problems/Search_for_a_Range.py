'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
This problem can be solved by binary search.
More specifically:
1. find the index of the first number >= target.
2. If cannot find or the number > target, return [-1,-1]
3. find the index of the first number >= target+1.
4. The end index is the above index-1
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if A == None or len(A) == 0:
            return [-1,-1]
        index1 = self.BS(A, target)
        if index1 == len(A) or A[index1] > target:
            return [-1,-1]
        index2 = self.BS(A, target+1)
        return [index1, index2-1]

    def BS(self, A, target):
        start = 0
        end = len(A)
        while start < end:
            if A[start] >= target:
                return start
            mid = (start+end)/2
            if A[mid] >= target:
                end = mid
            else:
                start = mid+1
        return end
    
A = []
target = 11
sol = Solution()
print sol.searchRange(A, target)