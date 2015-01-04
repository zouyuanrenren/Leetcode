'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        pos = [0] # i in pos iff s[:i] can be broken
        for i in range(1,len(s)+1):
            for word in dict:
                l = len(word)
                if i >= l and s[i-l:i] == word and i-l in pos:
                    pos.append(i)
                    break
        return len(s) in pos

sol = Solution()
s = "a"
dict = ["a", "code"]
print sol.wordBreak(s, dict)