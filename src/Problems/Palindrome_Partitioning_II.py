'''
Created on 2 Jan 2015

@author: Yuan
'''
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        miniK = []
        for i in range(len(s)+1):
            miniK.append(i-1)
        for i in range(len(s)):
            j = 0
            while i-j>=0 and i+j<len(s) and s[i-j] == s[i+j]:
                miniK[i+j+1] = min(miniK[i+j+1],1+miniK[i-j])
                j+=1
            j = 1
            while i-(j-1)>=0 and i+j<len(s) and s[i-(j-1)] == s[i+j]:
                miniK[i+j+1] = min(miniK[i+j+1], 1+miniK[i-j+1])
                j+=1
        return miniK[len(s)]



sol = Solution()
print sol.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")    