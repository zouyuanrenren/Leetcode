'''
Created on 30 Dec 2014

@author: Yuan
'''
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(S) < len(T):
            return 0
        ways = []
        for i in range(len(S)):
            row = []
            for j  in range(min(i+1,len(T))):
                if i > j:
                    row.append(ways[i-1][j])
                else:
                    row.append(0)
                if S[i] == T[j]:
                    if i > 0 and j > 0:
                        row[j]+=ways[i-1][j-1]
                    else:
                        row[j] += 1
            ways.append(row)
        return ways[len(S)-1][len(T)-1]

sol = Solution()
print sol.numDistinct("ABCDE", "AEC")