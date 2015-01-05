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

A array can have the following possibilities:
1. if the num[mid] < num[high]. Then minimum in the first part
2. if the num[mid] > num[high]. Then minimum in the 2nd part
3. if the num[mid] == num[high]. Then the minimum can be in both part. 
    a. First test the first part. If it is smaller than num[mid], then we found an answer.
    b. If not, then it is in the second part.

In worst case, the algorithm runs in O(n). In average case, the algorithm runs in O(logn)
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        return self.minimal(num,0,len(num)-1)
    def minimal(self,num,low, high):
        while low < high:
            mid = low + (high-low)/2
            if num[mid] > num[high]:
                low = mid+1
            elif num[mid] < num[high]:
                high = mid
            else:
                firstlow = self.minimal(num, low, mid)
                if firstlow < num[mid]:
                    return firstlow
                else:
                    return self.minimal(num, mid+1, high)
        return num[low]

    
print Solution().findMin([3,4,5,1,1,2,3])