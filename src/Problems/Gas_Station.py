'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
This problem can be solved with greedy strategy.
Assuming one can go up to gas station i with totgalgas and totalcost, 
    then one can go one stop further iff totalgas+gas[i] >= totalcost+cost[i]
    if not, then any station before i won't be able to support a round trip, we need to start from the next station 
If we start testing the station from 0, then all stations before the current station station have failed
    hence the attempt should stop when the next start is <= the current start
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