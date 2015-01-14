'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
This problem can be solved by dynamic programming.
We can use a matrix match to denote if a prefix of s can be matched to a prefix of p.
match[i][j] = True iff s[:i] can be matched to p[:j]
The the value of match is as follows:
    1. match[0][0] = True
    2. match[0][i+1] = True only when p[i] = "*" and
        a. match[0][i] = True, in this case, the last * does not need to match anything
        b. match[0][i-] = True, in this case, the last two "x*" do not match anything
    3. match[i+1][0] = False
    4. match[i+1][j-1] = True only when one of the following occurs:
        a. match[i][j] = True, and s[i] = p[j] or p[j] = "."
        b. p[j] = "*", and match[i+1][j] = True, in this case, the last "*" in p does not need to match
        c. p[j] = "*", and match[i+1][j-1] = True, in this case, the last two "x*" in p does not need to match
        d. p[j] = "*", and match[i][j+1] = True, and s[j] = p[i-1] or p[i-1] = ".".
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
                    if match[i+1][j] or match[i+1][j-1] or (match[i][j+1] and (s[i] == p[j-1] or p[j-1] == ".")):
                        match[i+1][j+1] = True
        return match[len(s)][len(p)]
    
print Solution().isMatch("aa", "a")