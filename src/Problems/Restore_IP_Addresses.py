'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        self.restore(s, 0, result, [])
        return result
    
    def restore(self, s, start, result, current):
        if start == len(s) and len(current) == 4:
            result.append(".".join(current))
            return
        if start == len(s) or len(current) == 4:
            return
        sum = 0
        while start < len(s) and sum * 10 + int(s[start]) < 256:
            sum = sum*10 + int(s[start])
            current.append(str(sum))
            self.restore(s, start+1, result, current)
            current.pop()
            start+=1
            if sum == 0:
                break
            
print Solution().restoreIpAddresses("010010")