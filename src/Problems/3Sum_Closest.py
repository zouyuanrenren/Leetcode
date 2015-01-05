'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
basic idea is same as 3Sum.
in addition, maintain the current closest one
for each sum found, update the closest one accordingly
then proceed the pointer moving
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
        index1 = 0
        while index1 < len(num) -2:
            index2 = index1+1
            index3 = len(num)-1
            while index2 < index3:
                SUM = num[index1]+num[index2]+num[index3]
                if abs(SUM-target) < abs(closest -target):
                    closest = SUM
                if SUM == target:
                    return target
                elif SUM > target:
                    index3 -= 1
                    while index2 < index3 and num[index3] == num[index3+1]:
                        index3 -= 1
                else:
                    index2 +=1
                    while index2 < index3 and num[index2] == num[index2-1]:
                        index2 += 1
            index1 += 1
            while index1 < len(num)-2 and num[index1] == num[index1-1]:
                index1 += 1
        return closest
