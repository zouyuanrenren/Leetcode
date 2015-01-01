'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        l = 0
        str = ""
        for c in s:
            if c in str:
                l = max(l, len(str))
                index = str.index(c)
                str = str[index+1:]
            str+=c
        return max(l, len(str))
    
print Solution().lengthOfLongestSubstring("abcabcbb")