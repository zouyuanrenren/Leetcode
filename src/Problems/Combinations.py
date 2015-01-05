'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
A typical back-tracking problem.
Points to note:
1. when add new items into the current solution, such item should be early enough in the candidate list
    so that there are sufficient elements left for the rest of the solution
2. candidate solution does not need to be re-created each time, it can be appended and popped. This saves space and time.
3. only when add a solution into result one need to create a new one.
'''
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        nums = range(1,n+1)
        results = []
        current = []
        self.combineList(results,current,nums,0,k)
        return results
    
    def combineList(self,results,current,nums,next,k):
        if k == 0:
            results.append(current[:])
            return
        for i in range(next, len(nums)+1-k):
            current.append(nums[i])
            self.combineList(results, current, nums, i+1, k-1)
            current.pop()
            
