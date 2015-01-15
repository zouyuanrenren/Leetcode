'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
This problem can be solved by binary search.
Note that the array has no duplicate and is sorted and rotated.
It can be shown that the following holds:
1. A[mid] == target    found
2. A[mid] <= A[end]    turning point of the array is before mid
    a. if A[mid] < target <= A[end]    start = mid +1
    b. otherwise    end = mid
3. A[mid] > A[end]    turning point of the array is after mid
    a. if A[start] <= target < A[mid]    end = mid
    b. otherwise    start = mid+1
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        start = 0
        end =len(A)
        while start < end:
            mid = (start+end)/2
            if A[mid] == target:
                return mid
            if A[mid] <= A[end-1]:
                if A[mid] < target and target <= A[end-1]:
                    start = mid+1
                else:
                    end = mid
            else:
                if A[start] <= target < A[mid]:
                    end = mid
                else:
                    start = mid+1
        return -1

A = [3,1]
target = 3
print Solution().search(A, target)