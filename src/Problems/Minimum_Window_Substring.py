'''
Created on 2 Jan 2015

@author: Yuan
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