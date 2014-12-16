'''
Created on 22 Nov 2014

@author: zouyuanrenren
'''

'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

'''
The basic idea is to first compute a subset, then add it if not duplicate
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        total = []
        if S == None:
            return None
        self.addsubset(total, [], S,0)
        return total
    
    def addsubset(self,total,current,S,index):
        if index == len(S):
            current.sort()
            self.addIfNotDuplicate(total, current)
        else:
            newcurrent1 = current[:]
            self.addsubset(total, newcurrent1, S, index+1)
            newcurrent2 = current[:]
            newcurrent2.append(S[index])
            self.addsubset(total, newcurrent2, S, index+1)        
            
    def addIfNotDuplicate(self,total,current):
        for list in total:
            if len(list) == len(current):
                same = True
                for i in range(len(list)):
                    if list[i] != current[i]:
                        same = False
                        break
                if same == True:
                    return
        total.append(current)

print Solution().subsetsWithDup([1,2,2])