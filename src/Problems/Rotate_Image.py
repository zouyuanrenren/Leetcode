'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
Need to do rotation for a quarter of the image.
For each matrix[x][y] in the quarater, make the following change
matrix[x][y], matrix[n-1-y][x], matrix[n-1-x][n-1-y], matrix[y][n-1-x] = matrix[n-1-y][x], matrix[n-1-x][n-1-y], matrix[y][n-1-x], matrix[x][y]
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for x in range((n+1)/2):
            for y in range((n)/2):
                matrix[x][y], matrix[n-1-y][x], matrix[n-1-x][n-1-y], matrix[y][n-1-x] = matrix[n-1-y][x], matrix[n-1-x][n-1-y], matrix[y][n-1-x], matrix[x][y]
        return matrix

matrix = [[1,2],[3,4]]
print Solution().rotate(matrix)