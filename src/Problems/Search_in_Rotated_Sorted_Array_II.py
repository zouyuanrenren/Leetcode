'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
Similar as the Search in Rotated Sorted Array, this problem can also be solved with binary search.
It can be shown that the following holds:
1. A[mid] = target,    found
2. A[mid] < A[end],    turning point of the array is before mid
    a. if A[mid] < target <= A[end]    start = mid +1
    b. otherwise    end = mid
3. A[mid] > A[end]    turning point of the array is after mid
    a. if A[start] <= target < A[mid]    end = mid
    b. otherwise    start = mid+1
4. A[mid] == A[end]    turning point of the array can be either before or after mid
    a. try to find target in the first part
    b. if not possible, try to find target in the second part
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        return self.searchin(A,target,0,len(A))
    def searchin(self,A,target,start,end):
        if start >= end:
            return False
        mid = (start+end)/2
        if A[mid] == target:
            return True
        if A[mid] < A[end-1]:
            if A[mid] < target <= A[end-1]:
                return self.searchin(A, target, mid+1, end)
            else:
                return self.searchin(A, target, start, mid)
        elif A[mid] > A[end-1]:
            if A[start] <= target < A[mid]:
                return self.searchin(A, target, start, mid)
            else:
                return self.searchin(A, target, mid+1, end)
        else:
            return self.searchin(A, target, start, mid) or self.searchin(A, target, mid+1, end)

A = [4,4,4,4,5,2,3]
target = 3
print Solution().search(A, target)
        