'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
A typical backtracking problem.
Let "current" be a partial candidate permutation.
Add elements in "num"-"current" to "current" one by one until "current" contains all elements, in which case a solution is found.
'''
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        List = []
        self.permuteList(List,[],num)
        return List
    def permuteList(self,List,current,numbers):
        if len(current) == len(numbers):
            List.append(current)
        else:
            for item in numbers:
                if item not in current:
                    self.permuteList(List, current+[item], numbers)
