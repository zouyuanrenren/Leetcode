'''
Created on 22 Nov 2014

@author: zouyuanrenren
'''

'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

'''
The basic idea is still dynamic programming, similar to Unique_Path.
The only difference is to consider the obstacle, the unique path to a obstacle is 0
'''

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        matrix = []
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[0][0] != 1:
            matrix.append([1])
        else:
            return 0
        for i in range(1, col):
            if obstacleGrid[0][i] == 0:
                matrix[0].append(matrix[0][i-1])
            else:
                matrix[0].append(0)
        for i in range(1, row):
            if obstacleGrid[i][0] == 0:
                matrix.append([matrix[i-1][0]])
            else:
                matrix.append([0])
            for j in range(1, col):
                if obstacleGrid[i][j] == 0:
                    matrix[i].append(matrix[i-1][j]+matrix[i][j-1])
                else:
                    matrix[i].append(0)
        return matrix[row-1][col-1]
    

matrix = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

print Solution().uniquePathsWithObstacles(matrix)
