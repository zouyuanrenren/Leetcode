'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
This problem can be solved with two-pointers.
Starting from the beginning and end of the string, and compare the next two valid characters until the pointers meet.
'''
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        S = s.lower()
        start = 0
        end = len(S) -1
        while start < end:
            compare = True
            c = S[start]
            if not((c >= 'a' and c <= 'z') or (c >= '0' and c <= '9')):
                start += 1
                compare = False
            t = S[end]
            if not((t >= 'a' and t <= 'z') or (t >= '0' and t <= '9')):
                end -= 1
                compare = False
            if compare:
                if c != t:
                    return False
                start += 1
                end -= 1
        return True

print Solution().isPalindrome("a ba")