'''
Created on 2 Jan 2015

@author: Yuan
'''
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        candi = []
        for num in range(n):
            candi.append(num+1)
        k -= 1
        result = ""
        div = {0:1}
        for i in range(1,10):
            div[i] = div[i-1]*i
        num = n-1
        while len(candi)>0:
            index = k/div[num]
            result+=str(candi[index])
            candi.remove(candi[index])
            k %= div[num]
            num -= 1
        return result

sol = Solution()
for i in range(1,10):
    print sol.getPermutation(5, i)