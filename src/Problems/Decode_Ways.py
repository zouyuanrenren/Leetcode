'''
Created on 30 Dec 2014

@author: Yuan
'''
'''
need to consider a few corner cases.
We use ways[i] to represent the number of ways for s[:i+1]:
1. first consider ways[0]
    = 0  if s[0] = 0
    = 1 otherwise
2. then consider ways[1]
    = 0 if s[0:2] > 20
    = 2 if s[0:2] between 11, 26
    = 1 otherwise
3. then consider ways[i]
'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if s == None or len(s) == 0:
            return 0
        if int(s[0]) == 0:
            return 0
        if len(s) == 1:
            return 1
        ways = [1]
        if int(s[1]) == 0:
            if int(s[0]) > 2:
                return 0
            else:
                ways.append(1)
        elif int(s[1]) > 6:
            if int(s[0]) > 1:
                ways.append(1)
            else:
                ways.append(2)
        else:
            if int(s[0]) < 3:
                ways.append(2)
            else:
                ways.append(1)
        for i in range(2, len(s)):
            num = int(s[i])
            pre = int(s[i-1])
            if num ==0:
                if pre == 0 or pre > 2:
                    return 0
                else:
                    ways.append(ways[i-2])
            elif num > 6:
                if pre == 0 or pre > 1:
                    ways.append(ways[i-1])
                else:
                    ways.append(ways[i-2]+ways[i-1])
            else:
                if pre == 0 or pre > 2:
                    ways.append(ways[i-1])
                else:
                    ways.append(ways[i-2]+ways[i-1])
        return ways[len(s)-1]
    
sol = Solution()
print sol.numDecodings("12120")