'''
Created on 30 Dec 2014

@author: Yuan
'''
'''
A typical dynamic programming problem.
We use ways[i][j] to denote the number of distinct subsequences of T[:j] in S[:i]
Obviously, ways[0][0] = 1 and ways[0][i] = 0 for any i > 0
Also, ways[i][0] = 1
And ways[i][j] = ways[i-1][j] + (ways[i-1][j-1] if S[i-1] == T[j-1])
'''
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(S) < len(T):
            return 0
        ways = [[0]*(len(T)+1)]
        ways[0][0] = 1
        for i in range(len(S)):
            row = [1]
            for j in range(len(T)):
                row.append(ways[i][j+1])
                if S[i] == T[j]:
                    row[j+1] += ways[i][j]
            ways.append(row)
        return ways[len(S)][len(T)]

sol = Solution()
print sol.numDistinct("rabbbit", "rabbit")