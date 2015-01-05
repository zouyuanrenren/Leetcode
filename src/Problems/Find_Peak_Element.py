'''
Created on 1 Jan 2015

@author: Yuan
'''

'''
A binary search solution is available:
1. if mid < mid +1, there must be peak in the second half.
2. if mid > mid +1, there must be peak in the first half.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 0:
            return None
        low = 0
        high = len(num)-1
        while low <= high:
            mid = (low+high)/2
            if mid == high:
                return mid
            if num[mid] < num[mid+1]:
                low = mid+1
            else:
                high = mid
        return low
                         

print Solution().findPeakElement([2,3,4,5])

