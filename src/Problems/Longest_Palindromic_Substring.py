'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
An O(n) solution can be found at http://www.felix021.com/blog/read.php?2040
The following shows an O(n^2) brutal force solution
'''
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if s == None:
            return None
        if len(s) <= 1:
            return s
        maxlength = 1
        maxstartpointer = 0
        currentpivot = 1
        while True:
            if 1+2*min(currentpivot, len(s)-currentpivot-1) > maxlength:
                half = 0
                while s[currentpivot - half] == s[currentpivot + half]:
                    half += 1
                    if half > currentpivot or currentpivot + half == len(s):
                        break
                if 2 * (half-1)+1 > maxlength:
                    maxlength = 2*(half-1)+1
                    maxstartpointer = currentpivot-half+1
            if 2*min(currentpivot,len(s)-currentpivot) > maxlength:
                half = 0
                if s[currentpivot] == s[currentpivot-1]:
                    while s[currentpivot - half-1] == s[currentpivot+half]:
                        half+= 1
                        if currentpivot-half-1 < 0 or currentpivot+half == len(s):
                            break
                if 2 * half > maxlength:
                    maxlength = 2 * half
                    maxstartpointer = currentpivot - half
            currentpivot += 1
            if currentpivot == len(s):
                break
        return s[maxstartpointer:maxstartpointer+maxlength]