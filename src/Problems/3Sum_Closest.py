'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
basic idea is same as 3Sum.
in addition, maintain the current closest one
for each sum found, update the closest one accordingly
then proceed the pointer moving

Slightly different from 3Sum, here we find the next different ni if a different way.
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSumClosest(self, num, target):
        if len(num) < 3:
            return []
        num.sort()
        closest = sum(num[0:3])
        if closest > target:
            return closest
        p1 = 0
        while p1 < len(num) -2:
            p2 = p1+1
            p3 = len(num)-1
            while p2 < p3:
                SUM = num[p1]+num[p2]+num[p3]
                if abs(SUM-target) < abs(closest -target):
                    closest = SUM
                if SUM == target:
                    return target
                elif SUM > target:
                    p3 -= 1
                    # find the next different n3
                    while p2 < p3 and num[p3] == num[p3+1]:
                        p3 -= 1
                else:
                    p2 +=1
                    # find the next different n2
                    while p2 < p3 and num[p2] == num[p2-1]:
                        p2 += 1
            p1 += 1
            # find the next different n1
            while p1 < len(num)-2 and num[p1] == num[p1-1]:
                p1 += 1
        return closest

num = [1,2,4,8,16,32,64,128]
target = 82

print Solution().threeSumClosest(num, target)