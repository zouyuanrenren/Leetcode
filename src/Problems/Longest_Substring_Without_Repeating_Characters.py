'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
Use a map to maintain the last position of a character
When encounter a character i:
    1. if c not in the map or the last position of c is beyond the current length l:
        l ++
    2. otherwise, c cannot be included into the current substring
        the current substring must re-start from the next character of previous c
        l = i - map[c]
        max length needs to be updated
Note that after iterating all c, there can be a final sub-string left.
    max length needs to be updated.
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        l = 0
        map = {}
        Maxl = 0
        for i in range(len(s)):
            c = s[i]
            if c not in map or i-map[c]>l:
                l += 1
            else:
                Maxl = max(Maxl, l)
                l = i-map[c]
            map[c] = i
        return max(Maxl, l)
    
print Solution().lengthOfLongestSubstring("abcabcbb")