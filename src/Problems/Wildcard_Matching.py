'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
this problem can be solved using a greedy algorithm:
suppose p[i] =p[j] = "*", where i < j, then p[i+1:] can match some s[m:] only if p[j+1:] can match some s[n:], where n > m.
consider the following, where | separates matching sub-strings:
S: ...|a...|b...|c...
P: ...|*a...|*b...|d...
now there are 4 possible ways to do adjustment:
 1. matching [a...] in S with [*a...] in P:
    in this case, there must be a sub-string after b in S that matches [b...d...] in P. Hence [b...c...] in S can be matched
    with [*b...d...] in P
 2. matching [a...] in S with [*b...] in P:
    similar as the above case, there must be a sub-string that matches [b...d...] in P. Hence [b...c...] matches [*b...d...]
 3. matching [b...] in S with [*a...] in P:
    similar as the above case, there must be a sub-string after b in S that matches [b...d...] in P.
 4. matching [b...c...] in S with [*b...d...] in P
    This indicates that we only need to remember the position of the last * and its matching pointer in S
'''
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        lastS = None
        lastM = None
        i1 = 0
        i2 = 0
        while i1 < len(s):
            if i2 < len(p) and (s[i1] == p[i2] or p[i2] == "?"): # find exact matching or ? matching
                i1+=1
                i2+=1
            elif i2 < len(p) and p[i2] == "*": # find *, we skip it in pattern
                lastS = i2
                lastM = i1
                i2 += 1
            elif lastS != None: # when mismatch found, revert to the last *, and use it to match the last matching char
                lastM += 1
                i1 = lastM
                i2 = lastS
            else:
                return False
        while i2 < len(p):
            if p[i2] != "*":
                return False
            i2 += 1
        return True

sol = Solution()
print sol.isMatch("aa", "")