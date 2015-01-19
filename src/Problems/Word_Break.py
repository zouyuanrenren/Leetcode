'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
This problem can be solved with dynamic programming:
We use a list pos to maintain the substrings that can be broken into the words in dict.
Particularly, i in pos IFF s[:i] can be broken.
Hence the following holds:
1. 0 in pos;
2. i in pos if there is some word in dict s.t. s[i-len(word):i] == word and i-len(word) in pos
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