'''
Created on 30 Dec 2014

@author: Yuan
'''
'''
Pretty much the same as Combination Sum.
The only difference is that, when looking for the next element to add into the current solution, one should find the next DIFFERENT one
'''
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        results = []
        current = []
        self.combine(candidates, target, 0, results, current)
        return results
    
    def combine(self, candidates, target, start, results, current):
        if target == 0:
            results.append(current)
            return
        for index in range(start, len(candidates)):
            if index == start or candidates[index] > candidates[index -1]:
                if candidates[index] <= target:
                    self.combine(candidates, target-candidates[index], index+1, results, current+[candidates[index]])
                else:
                    break

sol = Solution()

print sol.combinationSum2([10,1,2,7,6,1,5], 8)