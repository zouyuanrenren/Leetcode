'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
The basic idea is:
1. split the string by " ".
2. reverse the list of words.
3. join the list with " ".
'''
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        list = s.split()
        return " ".join(list[::-1])
    
print Solution().reverseWords("   ")