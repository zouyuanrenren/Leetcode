'''
Created on 22 Nov 2014

@author: zouyuanrenren
'''

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

'''
Basic dynamic programming problem:
1. the unique path to grid[0][0] = 1
2. the unique path to grid[i][j] = unique path to [i-1][j]+unique path to [i][j-1]
3. need some care about the top row and top column, which always have 1 unique path
'''

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        matrix = []
        matrix.append([1]*n)
        for row in range(1,m):
            local = [1]
            for col in range(1,n):
                local.append(local[col-1]+matrix[row-1][col])
            matrix.append(local)
        return matrix[m-1][n-1]