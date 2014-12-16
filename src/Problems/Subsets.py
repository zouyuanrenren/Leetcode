'''
Created on 22 Nov 2014

@author: zouyuanrenren
'''

'''
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

'''
This can be done with backtracking
'''


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        total = []
        if S == None:
            return None
        self.addsubset(total, [], S,0)
        for item in total:
            item = item.sort()
        return total
    
    def addsubset(self,total,current,S,index):
        if index == len(S):
            total.append(current)
        else:
            newcurrent1 = current[:]
            self.addsubset(total, newcurrent1, S, index+1)
            newcurrent2 = current[:]
            newcurrent2.append(S[index])
            self.addsubset(total, newcurrent2, S, index+1)