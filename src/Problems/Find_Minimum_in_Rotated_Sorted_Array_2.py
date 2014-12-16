'''
Created on 22 Nov 2014

@author: zouyuanrenren
'''


'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''

'''
Similar as Find_Minimun_in_Rotated_Sorted_Array, this problem can still be solved by binary search,
and actually by using exactly the same code:
1. if a sub-array's start is smaller than its end, then the start element is the minimal;
2. otherwise, perform binary search
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
    
    
print Solution().findMin([3,4,5,1,1,2,3])