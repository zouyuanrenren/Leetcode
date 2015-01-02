'''
Created on 2 Jan 2015

@author: Yuan
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