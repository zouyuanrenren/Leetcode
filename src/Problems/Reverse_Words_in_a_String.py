'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        result = []
        s += " a"
        current = ""
        for c in s:
            if c == " ":
                if len(current) > 0:
                    result.append(current)
                    current = ""
            else:
                current += c
        return " ".join(result[::-1]) 
    
print Solution().reverseWords("  ")