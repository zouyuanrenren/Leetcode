'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
This problem is similar to the Jump Game.
1. initial position = 0
2. initial step = 0
2. initial reachable position with step: = 0
3. initial next maximal position: = 0
5. for each reachable position i:
    i. the next maximal position = max(current maximal position, A[i]+i)
    ii. if i == current reachable position with step, then
        a. current reachable position with step = next maximal posisiotn
        b. current step += 1
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) == 0:
            return 0
        reachable = 0
        maxdist = 0
        current = 0
        step = 0
        while current <= reachable and current < len(A):
            maxdist = max(maxdist, A[current]+current)
            if current == reachable and current < len(A)-1:
                reachable = maxdist
                step+=1
            current += 1
        return step
    
print Solution().jump([1,2])