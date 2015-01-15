'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
Given the properties of the matrix, the basic idea is as follows:
1. find the first row whose first element is no smaller than the target:
    a. if it equals to the target, return True
    b. otherwise the previous row is where the target can be
2. if there is no previous row, then return False
3. in the previous row, perform binary search
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        row = 0
        while row < len(matrix):
            if matrix[row][0] == target:
                return True
            if matrix[row][0] > target:
                break
            row += 1
        row -= 1
        if row == -1:
            return False
        begin = 0
        end = len(matrix[row])
        while begin < end:
            mid = (begin+end)/2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                begin = mid + 1
            else:
                end = mid
        return False
