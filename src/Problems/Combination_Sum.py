'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
This is a typical back-tracking problem. The basic idea is:
1. first sort the candidates as results need to be in none-decending order
2. attempt to find target from 0 with current solution []

when attempt to find target from position k with current solution C, possibilities are:
1. target == 0, then found an answer, add C into to results
2. target < 0, over-combined, return
3. target > 0, for i = k, k+1, ..., attempt to find target-candidate[i] from position i with current solution C+candidate[i], 
    then backtrack to C
'''
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        List = []
        next = []
        self.combineList(List,next,candidates,0,target)
        return List
    
    def combineList(self,List,next,nums,k,target):
        if target == 0:
            List.append(next)
            return
        elif target < 0:
            return
        else:
            for index in  range(k,len(nums)):
                newNext = next[:]
                newNext.append(nums[index])
                if target >= nums[index]:
                    self.combineList(List, newNext, nums, index, target - nums[index])
                else:
                    break
