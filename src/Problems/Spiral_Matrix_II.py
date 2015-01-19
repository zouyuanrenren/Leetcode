'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
Two possible solutions:
1. go through 1 ... n**2, fill them into the cell of the matrix;
2. go through the matrix in a spiral order, fill the numbers incrementally;

In this program we go for the first solution.
'''
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        horizontal = True
        forward = True
        row = 0
        col = 0
        num = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        for num in range(1,n ** 2+1):
            matrix[row][col] = num
            if horizontal:
                if forward:
                    if col + 1 >= n or matrix[row][col+1] > 0:
                        horizontal = False
                        row += 1
                    else:
                        col += 1
                else:
                    if col -1 < 0 or matrix[row][col -1] > 0:
                        horizontal = False
                        row -= 1
                    else:
                        col -= 1
            else:
                if forward:
                    if row + 1 >= n or matrix[row+1][col] > 0:
                        horizontal = True
                        forward =  False
                        col -= 1
                    else:
                        row += 1
                else:
                    if row - 1 < 0 or matrix[row-1][col] > 0:
                        horizontal = True
                        forward = True
                        col += 1
                    else:
                        row -= 1
        return matrix
    
print Solution().generateMatrix(4)