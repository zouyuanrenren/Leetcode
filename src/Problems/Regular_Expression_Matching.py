'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        match = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        match[0][0] = True
        for j in range(len(p)):
            if p[j] == "*" and j > 0 and (match[0][j-1] or match[0][j]):
                match[0][j+1] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == ".":
                    if match[i][j]:
                        match[i+1][j+1] = True
                elif p[j] == "*" and j > 0:
                    if match[i+1][j] or match[i+1][j-1] or ((match[i][j] or match[i][j+1] or match[i][j-1]) and (s[i] == p[j-1] or p[j-1] == ".")):
                        match[i+1][j+1] = True
        return match[len(s)][len(p)]
    
print Solution().isMatch("aa", "a*")