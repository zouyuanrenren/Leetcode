'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
Similar as Pascals Triangle.
The difference is that we don't need to return the triangle but only the last row.
So we can simplify the storage to maintain only the previous and current row.
'''
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        pre = [1]
        if rowIndex == 0:
            return pre
        for i in range(1, rowIndex+1):
            current = [1]
            for j in range(1, i):
                current.append(pre[j]+pre[j-1])
            current.append(1)
            pre = current
        return current