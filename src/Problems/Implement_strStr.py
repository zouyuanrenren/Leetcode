'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
Classical string matching problem.
One can use classic algorithms such as KMP.
But here we use a brutal force algorithm.
To save some time, we can always compare from the last character of the needle and move backward
    stop when it matches all characters or a mismatch is found
    if all characters are matched, then we can return the pointer
    otherwise, we move forward one step in the hay
'''
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack):
            return None
        if len(needle) == 0:
            return haystack
        pointer = len(haystack)
        for i in range(len(needle)-1,len(haystack)):
            index = 0
            while needle[len(needle)-1-index] == haystack[i-index]:
                index += 1
                if index == len(needle):
                    break
            if index == len(needle):
                pointer = i - index +1
                break
        if pointer == len(haystack):
            return None
        else:
            return haystack[pointer:]