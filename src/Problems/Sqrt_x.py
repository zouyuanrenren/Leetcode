'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
This is a binary search problem.
1. initially low = 0, high = x;
2. if mid ** 2 > x, high = mid-1;
3. if mid ** 2 < x, low = mid+1;
4. if mid ** 2 == x, return mid
when loop finished and cannot find the right mid, return high-1 if high ** 2 > x, otherwise return high
'''
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        low = 0
        high = x
        while low < high:
            mid = low +(high-low)/2
            mid2 = mid * mid
            if mid2 == x:
                return mid
            if mid2 < x:
                low = mid+1
            else:
                high = mid-1
        if high * high > x:
            return high -1
        return high

sol = Solution()
for i in range(10):
    print sol.sqrt(i*1000)