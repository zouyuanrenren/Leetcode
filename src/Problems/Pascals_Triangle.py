'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
The triangle is as follows:
1
11
121
1331
14641
...

when row >= 2, for each row, the jth element = j-1th element + jth element of the previous row.
'''
class Solution:
    # @return a list of integers
    def generate(self, numRows):
        results = []
        if numRows > 0:
            results.append( [1])
        for i in range(1,numRows):
            List = [1]
            for j in range(1,i):
                List.append(results[-1][j]+results[-1][j-1])
            List.append(1)
            results.append(List)
        return results
    
print Solution().generate(6)   