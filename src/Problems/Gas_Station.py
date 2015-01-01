'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        start = 0
        totalgas = 0
        totalcost = 0
        current = 0
        length = len(gas)
        while True:
            totalgas += gas[current]
            totalcost += cost[current]
            if totalgas >= totalcost:
                current = (current+1)%length
                if current == start:
                    return start
            else:
                current = (current+1)%length
                if start >= current:
                    return -1
                start = current
                totalgas = 0
                totalcost = 0

sol = Solution()

print sol.canCompleteCircuit([4], [5])            