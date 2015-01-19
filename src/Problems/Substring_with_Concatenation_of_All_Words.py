'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
words in L may appear multiple times, hence we can use a dictionary to count the appearance of words in L.
For each index in S, we can create a dictionary for the next len(L) words and see if the count is the same as in the dictionary.
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
            count = {}
            for j in xrange(len(L)):
                word = S[i+j*l:i+j*l+l]
                if word in dict and (word not in count or count[word] < dict[word]):
                    count[word] = 1 if word not in count else count[word]+1
                else:
                    count = {}
                    break
            if count:
                result.append(i)
        return result
        
    
sol = Solution()
S = "barfoothefoobarman"
L = ["foo", "bar"]
print sol.findSubstring(S, L)