'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        maxarea = 0
        stack = [0]
        height.append(0)
        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                maxarea = max(maxarea, h*w)
            stack.append(i)
        return maxarea
    
print Solution().largestRectangleArea([1])