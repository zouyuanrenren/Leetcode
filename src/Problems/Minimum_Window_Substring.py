'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
This problem utlises several techniques.
1. To know that a substring include all characters in the patter, one need to remember how many times each character
    appears in the substring and the pattern.
    Hence a dictionary is needed, which preserves the number of appearance of each character in the pattern.
2. To maintain the current string, a two-pointer pair can be used:
    one pointer c indicates the next character to include.
    another pointer nc indicates the next character to remove.
3. Combine the above two:
    when c is included into the current string, one needs to check how many times c have been included.
    If all characters have been included for the respective times, then the candidate string is found.
    Otherwise c moves forward.
    When a candidate string is found, one need to check if nc can be removed.
    If nc can be removed, then move nc forward and we will get a new candidate string.
'''
class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) < len(T):
            return ""
        dict = {}
        for c in T:
            dict[c] = 1 if c not in dict else dict[c]+1
        totalc = len(dict)
        current = ""
        mini = None
        for c in S:
            current += c
            if c in dict:
                dict[c] -= 1
                if dict[c] == 0:
                    totalc -= 1
                    if totalc == 0:
                        if mini == None or len(mini) > len(current):
                            mini = current
                if totalc == 0:
                    for nc in current:
                        if nc not in dict or dict[nc] < 0:
                            current = current[1:]
                            if nc in dict:
                                dict[nc] += 1
                        else:
                            break
                    if mini == None or len(mini) > len(current):
                        mini = current
        if mini == None:
            return ""
        return mini

S = "a"
T = "b"
print Solution().minWindow(S, T)