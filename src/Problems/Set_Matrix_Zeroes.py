'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
The key to this problem is to separate the original "0" and affected "0".
A cell on the row or column of a original "0" should be set to an affected "0".
A cell only on the row or column of an affected "0" should not be affected.

The problem can have the following solutions:
1. using a separate O(mn) matrix to maintain the results;
2. using a separate O(m+n) array to maintain the affected row and column, i.e. positions of the original "0"s;
3. changing the original or affected "0" into some other special symbols. This symbol can be None or a value smaller/larger than the min/max.
4. using the joint of two original "0"s to indicate the affected row and column.

In the following Solution we use the above option 4.
In the following Solution2 we use the above option 3.
'''
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        pivotrow = -1
        pivotcol = -1
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    if pivotrow == -1:
                        pivotrow = row
                        pivotcol = col
                    else:
                        matrix[pivotrow][col] = 0
                        matrix[row][pivotcol] = 0
        if pivotrow != -1:
            for row in range(len(matrix)):
                if row != pivotrow:
                    for col in range(len(matrix[row])):
                        if col != pivotcol:
                            if matrix[row][pivotcol] == 0 or matrix[pivotrow][col] == 0:
                                matrix[row][col] = 0
            for col in range(len(matrix[pivotrow])):
                matrix[pivotrow][col] = 0
            for row in range(len(matrix)):
                matrix[row][pivotcol] = 0

class Solution2:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    for i in range(len(matrix)):
                        if matrix[i][col] != 0:
                            matrix[i][col] = None
                    for j in range(len(matrix[row])):
                        if matrix[row][j] != 0:
                            matrix[row][j] = None
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == None:
                    matrix[row][col] = 0    
