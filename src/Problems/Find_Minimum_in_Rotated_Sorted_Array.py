'''
Created on 22 Nov 2014

@author: zouyuanrenren
'''
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

'''
This problem can be solved with binary search:
An array can have 3 different possibilities:
1. in ascending order, in this case, the minimum is in the first half:
2. otherwise:
    a. the minimum in the first part. In this case, the middle element will be smaller than the last element
    b. the minimun in the second part. In this case, the middle element will be larger than the last element
    
Note that possibility 1 also have middle < last
We can apply recursion.
'''


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 0:
            return None
        low = 0
        high = len(num)-1
        while low < high:
            mid = low + (high-low)/2
            if num[mid] < num[high]:
                high = mid
            else:
                low = mid+1
        return num[low]
    
    
print Solution().findMin([4,5,1,2,3])