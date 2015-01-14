'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
Similar as the Permutation, using backtracking.
The difference is that:
In the Permutation, a candidate permutation can be appended with any remaining element.
While in this problem, due to the existence of duplicated elements, a candidate permutation can only be appended with unique elements.
'''
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        result = []
        self.perm(num, result, [])
        return result
    
    def perm(self, num, result, current):
        if len(num) == 0:
            result.append(current[:])
            return
        for i in range(len(num)):
            if i == 0 or num[i] != num[i-1]:
                # found a candidate
                candi = num[i]
                newNum = num[:i]+num[i+1:]
                current.append(candi)
                self.perm(newNum, result, current)
                current.pop()

sol = Solution()
result = sol.permuteUnique([1,1,2,1,2])
for p in result:
    print p            