'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
Next permutation can be found in the following way:
1. from right to left, find the first index currentI who has a larger element to its right
2. if currentI == -1, i.e., cannot be found, then the number is reversely sorted, we just need to sort it again.
3. if currentI is found, go find the minimal larger element swap to its right.
4. swap the position of currentI and swap.
5. sort the part to the right of the original position of currentI.
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