'''
Created on 6 Jan 2015

@author: Yuan
'''
'''
A typical dynamic programming problem.
Let us assume that there is a matrix HP of same size as dungeon.
And HP[i][j] represents the minimal hp for the knight to start from dungeon[i][j] while still able to see princess alive.
HP[0][0] will be the result of the problem.

Obviously, the following holds:
    1. when leaving dungeon[i][j], the knight should have min(HP[i+1][j], HP[i][j+1]) so that it can reach the princess alive.
        let us call it min[i][j]
    2. hence, the following two conditions must hold:
        HP[i][j] >= 1
        HP[i][j] + dungeon[i][j] >= min[i][j]
        so HP[j][j] = 1 if 1+ dungeon[i][j] > min[i][j] else min[i][j] - dungeon[i][j]

Note that the calculation of HP[i][j] requies min[i][j], i.e. HP[i+1][j] and HP[i][j+1].
Hence we can start the calculation from HP[-1][-1] to HP[0][0].
The corner cases will be the last column and last row of HP.

In order to save some space, we can actually reuse the original dungeon to maintain HP.
'''
class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if len(dungeon) == 0:
            return None
        
        h = len(dungeon)
        w = len(dungeon[0])
        
        # calculate the HP for the last cell
        dungeon[-1][-1] = 1-dungeon[-1][-1]
        if dungeon[-1][-1] < 1:
            dungeon[-1][-1] = 1
        
        # calculate the HP for the last row
        for col in range(w-1)[::-1]:
            dungeon[-1][col] = dungeon[-1][col+1] - dungeon[-1][col]
            if dungeon[-1][col] < 1:
                dungeon[-1][col] = 1

        # calculate the HP for the rest of the dungeon
        for row in range(h-1)[::-1]:
            # calculate the HP for the last col for each row
            dungeon[row][-1] = dungeon[row+1][-1]-dungeon[row][-1]
            if dungeon[row][-1] < 1:
                dungeon[row][-1] = 1
            # calculate the HP for the rest of the row
            for col in range(w-1)[::-1]:
                dungeon[row][col] = min(dungeon[row+1][col], dungeon[row][col+1]) - dungeon[row][col]
                if dungeon[row][col] < 1:
                    dungeon[row][col] = 1
        
        # return the result
        return dungeon[0][0]
    
dungeon = [[-2,-3,3],
           [-5,-10,1],
           [10,30,-5]]


print Solution().calculateMinimumHP(dungeon)

# should have updated dungeon as follows
[[7,5,2],
[6,11,5],
[1,1,6]]