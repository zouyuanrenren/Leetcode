'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
Examine the characters from the end to the beginning of the string.
If a word has started (with length > 0) and the character is " ", then we found a word and its length
Otherwise, if the character is not " ", then we increase the length by 1.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        current = 0
        for c in s[::-1]:
            if c == ' ' and current > 0:
                break
            elif c != ' ':
                current += 1
        return current
