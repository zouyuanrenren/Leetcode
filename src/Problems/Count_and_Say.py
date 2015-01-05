'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
One of the simple problems.
only need to compare with the previous character:
1. if the c == prec, then count ++
2. else add int(count)+c into the string, and set count = 1
3. remember to deal with the trailing characters.
'''
class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        pre = "1"
        current = "11"
        for i in range(3,n+1):
            pre = current
            current = ""
            prec = '5'
            count = 0
            for c in pre:
                if c == prec:
                    count +=1
                else:
                    if count > 0:
                        current+=str(count)
                        current+=prec
                    count = 1
                    prec = c
            if count > 0:
                current+=str(count)
                current+=prec
        return current
                