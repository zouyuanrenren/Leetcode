'''
Created on 22 Nov 2014

@author: zouyuanrenren
'''
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
'''
The basic idea is to use a pointer to traverse the matrix.
However, there are two ways to decide when to turn:
1. one is to use two variables row and col to maintain how many row or col the current pointer needs to travel before turn;
    when it turns the variables will be updated.
2. the other is to rewrite None into travelled cell. Then the pointer turns when it reaches None or border

In this solution we adopt the first approach
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == None:
            return None
        if len(matrix) == 0:
            return []
        row = len(matrix)
        col = len(matrix[0])
        currentrow = 0
        currentcol = -1
        horizontal = True
        forward = True
        result = []
        while row >0 and col >0:
            if horizontal:
                if forward:
                    for i in range(col):
                        currentcol+=1
                        result.append(matrix[currentrow][currentcol])
                else:
                    for i  in range(col):
                        currentcol -= 1
                        result.append(matrix[currentrow][currentcol])
                horizontal = False
                row -= 1
            else:
                if forward:
                    for i in range(row):
                        currentrow += 1
                        result.append(matrix[currentrow][currentcol])
                    forward = False
                else:
                    for i in range(row):
                        currentrow -= 1
                        result.append(matrix[currentrow][currentcol])
                    forward = True
                horizontal = True
                col -= 1
        return result
    
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print Solution().spiralOrder(matrix)
                        
                