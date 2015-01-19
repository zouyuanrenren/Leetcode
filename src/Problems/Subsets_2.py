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
There can be different solutions:
1. Solution1: The basic idea is to first compute a subset, then add it if not duplicate
2. Solution2: sort the list first, and when generating subset, the element of each specific index must be unique. 
'''

class Solution1:
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

print Solution1().subsetsWithDup([1,2,2])


class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        results = []
        self.sortfrom(S,results,[],0)
        return results
    
    def sortfrom(self, S, results, subset, index):
        if index == len(S):
            results.append(subset[:])
        else:
            subset.append(S[index])
            self.sortfrom(S, results, subset, index+1)
            subset.pop()
            index += 1
            while index < len(S) and S[index] == S[index-1]:
                index += 1
            self.sortfrom(S, results, subset, index)

print Solution2().subsetsWithDup([1,1,1,1,1])