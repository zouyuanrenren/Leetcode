'''
Created on 30 Dec 2014

@author: Yuan
''' 
'''
A typical dynamic programming problem.
We use a matrix mDs to maintain the minimal steps.
Particularly, mDs[i][j] represnets the minimal distance between word1[:i] and word2[:j]
Then obviously mDs[0] = [0,1,...]
For mDs[i][j], there are following possibilities:
    1. by removing the trailing character in word1, hence = mDs[i-1][j]+1
    2. by removing the trailing character in word2, hence = mDs[i][j-1]+1
    3. by replacing the last character in word1 with the one in word2, hence = mDs[i-1][j-1]+1
    4. when word1[i] == word2[j], and simply following previous steps, hence = mDs[i-1][j-1]
We only need to find the minimal of the 4.

In fact, matrix mDs can be replaced with 2 arrays since only the current and last row in mDs matter.
In fact, the two arrays can be replaced with a single one since only the current and previous position in the array matter.
'''
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        mDs = [range(len(word2)+1)]
        for i in range(len(word1)):
            row = [i+1]
            for j in range(len(word2)):
                current = min(mDs[i][j+1]+1, mDs[i][j]+1, row[j]+1)
                if word1[i] == word2[j]:
                    current = min(current, mDs[i][j])
                row.append(current)
            mDs.append(row)
        return mDs[len(word1)][len(word2)]
#         mDs = []
#         if len(word1) == 0:
#             return len(word2)
#         if len(word2) == 0:
#             return len(word1)
#         if word1[0] == word2[0]:
#             row = [0]
#         else:
#             row = [1]
#         for i in range(1, len(word2)):
#             if word1[0] == word2[i]:
#                 row.append(i)
#             else:
#                 row.append(row[i-1]+1)
#         mDs.append(row)
#         for i in range(1, len(word1)):
#             if word1[i] == word2[0]:
#                 row = [i]
#             else:
#                 row = [mDs[i-1][0]+1]
#             for j in range(1, len(word2)):
#                 if word1[i] == word2[j]:
#                     basic = mDs[i-1][j-1]
#                 else:
#                     basic = mDs[i-1][j-1]+1
#                 row.append(min(basic, mDs[i-1][j]+1, row[j-1]+1))
#             mDs.append(row)
#         return mDs[len(word1)-1][len(word2)-1]

sol = Solution()
print sol.minDistance("sea", "eat")