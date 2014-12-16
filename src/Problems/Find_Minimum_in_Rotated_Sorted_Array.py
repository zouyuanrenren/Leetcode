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
1. since there is no duplicate, every value is unique;
2. if a sub-array's start element is smaller than the sub-array's end element, then the min is the start element
3. otherwise, perform binary-search
'''


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        return self.minimal(num,0,len(num))
    def minimal(self,num,start,end):
        if start == end:
            return None
        if num[start] < num[end-1]:
            return num[start]
        if start == end-1:
            return num[start]
        mid = start+(end-start)/2
        return min(self.minimal(num, start, mid),self.minimal(num,mid,end))
    
    
print Solution().findMin([])