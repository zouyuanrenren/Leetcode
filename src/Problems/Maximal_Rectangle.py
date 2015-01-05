'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
This problem can be solved by using the solution in Largest Rectangle in Histogram
'''
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        height = [0]*len(matrix[0])
        height.append(0)
        result = 0
        for i in range(0, len(matrix)):
            for j in range(len(height)-1):
                height[j] = 0 if matrix[i][j] == "0" else height[j]+1
            result = max(result, self.largestRectangleArea(height))
        return result
    
    def largestRectangleArea(self, height):
        maxarea = 0
        stack = [0]
        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                maxarea = max(maxarea, h*w)
            stack.append(i)
        return maxarea

matrix = ["00", "00"]

print Solution().maximalRectangle(matrix)