'''
Created on 30 Dec 2014

@author: Yuan
'''
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        mDs = []
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if word1[0] == word2[0]:
            row = [0]
        else:
            row = [1]
        for i in range(1, len(word2)):
            if word1[0] == word2[i]:
                row.append(i)
            else:
                row.append(row[i-1]+1)
        mDs.append(row)
        for i in range(1, len(word1)):
            if word1[i] == word2[0]:
                row = [i]
            else:
                row = [mDs[i-1][0]+1]
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    basic = mDs[i-1][j-1]
                else:
                    basic = mDs[i-1][j-1]+1
                row.append(min(basic, mDs[i-1][j]+1, row[j-1]+1))
            mDs.append(row)
        return mDs[len(word1)-1][len(word2)-1]

sol = Solution()
print sol.minDistance("sea", "eat")