'''
Created on 3 Jan 2015

@author: Yuan
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
        for step in range(1, len(s1)+1):
            for i1 in range(0, len(s1)-step+1):
                for i2 in range(0, len(s2)-step+1):
                    if step == 1:
                        if s1[i1] == s2[i2]:
                            matrix[step][i1][i2] = True
                    else:
                        found = False
                        for newstep in range(1, step):
                            if matrix[newstep][i1][i2] and matrix[step-newstep][i1+newstep][i2+newstep]:
                                found = True
                                break
                            if matrix[newstep][i1][i2+step-newstep] and matrix[step-newstep][i1+newstep][i2]:
                                found = True
                                break
                        if found:
                            matrix[step][i1][i2] = True
        return matrix[len(s1)][0][0]
    
print Solution().isScramble("taerg", "great")
                    
