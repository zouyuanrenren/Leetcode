'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
This problem essentially asks to find i < j in range(len(height)) s.t. (j-i) * min(height[i], height[j]) is maximal.
The following several lemma holds:
1. if (i,j) is not maximal, then for any i<k<j s.t. height[k] <= height[i], (k,j) is not maximal.
    Hence, when looking of the next candidate i, we only need to look for the one with greater height
2. if (i,j) is not maximal, then for any i<k<j, s.t. height[k] <= height[j], (i,k) is not maximal.
    Hence, when looking for the next candidate j, we only need to look for the one with greater height
3. if (i,j) is not maximal and height[i] < height[j], then for any i<k<j s.t. height[k] >= height[j], (i,k) is not maximal.
    Hence, before looking for the next candidate j, we should first look for the next candidate i.
4. if (i,j) is not maximal and height[i] > height[j], then for any i<k<j s.t. height[k] >= height[i], (k,j) is not maximal.
    Hence, before looking for the next candiate i, we should first look for the next candiate j.

To summarise, we:
1. start from the left-most and right-most bars
2. always seek to look for the next candidate for the shorter bar
3. and the next candidate should always be higher than the current candiate
'''
class Solution:
    # @return an integer
    def maxArea(self, height):
        Max = 0
        if height == None or len(height) < 2:
            return 0
        i = 0
        j = len(height) - 1
        lastI = 0
        lastJ = j
        Max = (j-i) * min(height[j], height[i])
        while i < j:
            if height[j]<= height[i]:   # we should look for the next j
                if height[j] >= height[lastJ]:   # found a new candidate j
                    lastJ = j
                    Max = max(Max, (j-i)*min(height[j],height[i]))
                j -= 1
            else:   # we should look for the next i
                if height[i] >= height[lastI]:   # found a new candidate i
                    lastI = i
                    Max = max(Max, (j-i)*min(height[j], height[i]))
                i += 1
        return Max
    
print Solution().maxArea([2,3,10,5,7,8,9])