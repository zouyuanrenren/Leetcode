'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
This problem can be solved with dynamic programming.
we use matrix[i][j] to denote if s1[:i] and s2[:j] can be combined into s3[:i+j]
matrix[0]][0] = True
for i and j, matrix[i+1][j+1] = 
    matrix[i][+1j] and s1[i] == s3[i+j+1], 
    or matrix[i+1][j] and s2[j] == s3[i+j+1] 
'''
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2) != len(s3):
            return False
        matrix = []
        row = [True]
        for i in range(len(s2)):
            row.append(row[i] and s2[i] == s3[i])
        matrix.append(row)
        for i in range(len(s1)):
            row = [matrix[i][0] and s1[i] == s3[i]]
            for j in range(len(s2)):
                row.append((matrix[i][j+1] and s1[i] == s3[i+j+1]) or (row[j] and s2[j] == s3[i+j+1]))
            matrix.append(row)
        return matrix[len(s1)][len(s2)]

print Solution().isInterleave("a", "b", "a")