'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if len(L) == 0 or len(L[0]) == 0 or len(S) < len(L) * len(L[0]):
            return []
        l = len(L[0])
        dict = {}
        result = []
        for word in L:
            dict[word] = 1 if word not in dict else dict[word]+1
        for i in xrange(0,len(S)+1-l*len(L)):
            curr = {}
            for j in xrange(len(L)):
                word = S[i+j*l:i+j*l+l]
                if word in dict and (word not in curr or curr[word] < dict[word]):
                    curr[word] = 1 if word not in curr else curr[word]+1
                else:
                    curr = {}
                    break
            if curr:
                result.append(i)
        return result
        
    
sol = Solution()
S = "barfoothefoobarman"
L = ["foo", "bar"]
print sol.findSubstring(S, L)