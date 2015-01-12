'''
Created on 12 Jan 2015

@author: Yuan
'''
'''
A typical dynamic programming problem.
Let us use MIN[i][j] to represent the minimal path sum from grid[0][0] to grid[i][j]
then MIN[i][j] = min(MIN[i-1][j], MIN[i][j-1])+grid[i][j].
Consider the first row and column of grid[i][j] as corner cases.

Two options for optimisations like other DP problems:
1. using the original grid to maintain MIN.
2. If can't change the original grid, using two lists to maintain the previous and current row of MIN.
'''
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        l = len(grid)
        if l == 0:
            return 0
        w = len(grid[0])
        if w == 0:
            return 0
        MIN = [[grid[0][0]]]
        for i in range(1,w):
            MIN[0].append(MIN[0][-1]+grid[0][i])
        for row in range(1,l):
            newrow = [MIN[-1][0]+grid[row][0]]
            for col in range(1,w):
                newrow.append(grid[row][col]+min(MIN[row-1][col],newrow[-1]))
            MIN.append(newrow)
        return MIN[l-1][w-1]