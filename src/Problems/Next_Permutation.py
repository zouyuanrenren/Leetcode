'''
Created on 2 Jan 2015

@author: Yuan
'''
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) < 2:
            return num
        maxI = len(num)-1
        currentI = len(num)-1
        while currentI >= 0 and num[currentI] >= num[maxI]:
            if num[currentI] > num[maxI]:
                maxI = currentI
            currentI -= 1
        if currentI == -1:
            num.sort()
            return num
        else:
            swap = maxI
            for i in range(maxI, len(num)):
                if num[i] < num[swap] and num[i] > num[currentI]:
                    swap = i
            num[currentI], num[swap] = num[swap], num[currentI]
            part = num[currentI+1:len(num)]
            part.sort()
            for i in range(currentI+1,len(num)):
                num[i] = part[i-currentI-1]
        return num
    
print Solution().nextPermutation([1,2,3])