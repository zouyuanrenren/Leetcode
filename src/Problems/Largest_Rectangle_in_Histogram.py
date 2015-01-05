'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
This is a back tracking problem.
We can go through all position i, and compute the area of rectangle with height[i], then we keep the maximal area
To compute the area with height[i], we need to find the first j>i s.t. heigh[j] < height[i] and the first k<i s.t. height[k] < height[i]

So we can do the following
1. start with the stack = [0]
2. go through all the j in the array
    a. if height[j] > height[stack[-1]], then push it into the stack, and check the next j++
        by doing this, for every consecutive k, i in the stack, k is the first one with k < i and height[k] < height[i]
    b. if height[j] < height[stack[-1]], then we need to pop stack.
        by doing this, let i = stack.pop(), then j is the first j > i s.t. height[j] < height[i].
        in this case, the area of rectangle with height[i] = height[i] * (j-stack[-1]-1)
        we recurse part b until stack is empty or it does not hold
'''
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        maxarea = 0
        stack = [0]
        height.append(0)
        for j in range(1, len(height)):
            while stack and height[j] < height[stack[-1]]:
                h = height[stack.pop()]
                w = j if not stack else j - stack[-1] -1
                maxarea = max(maxarea, h*w)
            stack.append(j)
        return maxarea
    
print Solution().largestRectangleArea([1])