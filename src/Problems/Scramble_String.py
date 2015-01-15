'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
This problem can be solved with dynamic programming.
Given two strings s1[i1:j1] and s2[i2:j2] with same length
the later is a scramble of the former iff for some x in range(1,(j1-i1)), one of the following holds:
    1. s2[i2:i2+x] is a scramble of s1[i1:i1+x] and s2[i2+x:j2] is a scramble of s1[i1+x:j1].
    2. s2[i2:i2+x] is a scramble of s1[j1-x:j1] and s2[i2+x:j2] is a scramble of s1[i1:j1-x]

Hence, for each two substrings of s1 and s2 with same length, we can inductively compute if they are scramble of each other. 
We use a matrix to store such information.
    1. matrix[length][i][j] denotes if s1[i:i+length] is a scramble of s2[j:j+length]
    2. matrix[1][i][j] == True iff s1[i] = s2[j]
    3. matrix[length][i][j] = True iff there is some x s.t.
        a. matrix[x][i][j] and matrix[length-x][i+x][j+x]
        b. matrix[x][i][j+length-x] and matrix[length-x][i+x][j]

such a matrix can be built with increasing length so that values of all elements can be properly computed. 
'''
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) == 0:
            return len(s2) == 0
        if len(s2) == 0:
            return len(s1) == 0
        matrix = []
        for i in range(len(s1)+1):
            row = []
            for j in range(len(s1)):
                col = [False] * (len(s1))
                row.append(col)
            matrix.append(row)
        for length in range(1, len(s1)+1):
            for i in range(0, len(s1)-length+1):
                for j in range(0, len(s2)-length+1):
                    if length == 1:
                        if s1[i] == s2[j]:
                            matrix[length][i][j] = True
                    else:
                        found = False
                        for x in range(1, length):
                            if matrix[x][i][j] and matrix[length-x][i+x][j+x]:
                                found = True
                                break
                            if matrix[x][i][j+length-x] and matrix[length-x][i+x][j]:
                                found = True
                                break
                        if found:
                            matrix[length][i][j] = True
        return matrix[len(s1)][0][0]
    
print Solution().isScramble("taerg", "great")
                    
