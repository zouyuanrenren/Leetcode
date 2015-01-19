'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
A typical dynamic programming problem.
Let us use a list of lists mins to represent the minimal total for each position in the triangle.
Specially mins[i][j] is the minimal total for path from triangle[0][0] to triangle[i][j].
In a general case, mins[i][j] = triangle[i][j]+min(mins[i-1][j],mins[i-1][j-1])
The special cases are the first and last element of each row.
The final results would be the minimal of the last row of mins.

To save space, we can also use triangle to maintain mins.
If the original triangle cannot be changed, another way to save space is to only maintain the previous row of mins.
In that case, we only need to use O(n) extra space since the maximal size of the row is the height of the triangle 
In the following solution, we use this optimisation
'''
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if triangle == None:
            return 0
        if len(triangle) == 0:
            return 0
        mins = [triangle[0][0]]
        for i in range(1, len(triangle)):
            row = [mins[0]+triangle[i][0]]
            for j in range(1, len(triangle[i])-1):
                row.append(triangle[i][j]+min(mins[j], mins[j-1]))
            row.append(triangle[i][-1]+mins[-1])
            mins = row
        return min(mins)
