'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
for each character, go though the list of strings to find out if that character is the same in all strings.
'''
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        shortest = len(strs[0])
        for index in range(1,len(strs)):
            if len(strs[index]) < shortest:
                shortest = len(strs[index])
        string = ""
        include = True
        index = 0
        while include and index < shortest:
            c = strs[0][index]
            for i in range(1,len(strs)):
                include = include and strs[i][index] == c
                if not include:
                    break
            if include:
                string += c
            index +=1
        return string
