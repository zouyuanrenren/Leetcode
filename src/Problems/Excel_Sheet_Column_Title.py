'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @return a string
    def convertToTitle(self, num):
        title = []
        while num != 0:
            num -= 1
            title.append(chr(ord("A")+num%26))
            num = num/26
        title.reverse()
        return "".join(title)

sol = Solution()

for i in range(100):
    print i, sol.convertToTitle(i)