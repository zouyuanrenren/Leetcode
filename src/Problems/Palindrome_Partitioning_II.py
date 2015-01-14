'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
This can be solved with dynamic programming.
We use a list miniK to maintain the minimal cut. And miniK[i] represent the minimal cut for s[:i].
Obviously some corner cases are:
1. miniK[0] = -1, this is just auxiliary.
2. miniK[1] = 0, the first character does not require any cutting.
3. for each i, miniK[i] <= i-1, which is the worst case that cuts every character out.

Now for each character at position "i" in the string, 
    we can use it as the mid-character of a candidate palindrome and then expand on both directions with "j" characters.
    As long as the "j" character on its left is the same as the "j" character on its right, the substring s[i-j:i+j+1] is a parlindrome.
    And miniK[i+j+1] = min(miniK[i+j+1], 1+miniK[i-j])
    
    The above is for palindrome with odd number of characters, with even numbers it is slightly different.

'''
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        miniK = []
        for i in range(len(s)+1):
            miniK.append(i-1)
        for i in range(len(s)):
            j = 0
            while i-j>=0 and i+j<len(s) and s[i-j] == s[i+j]:
                miniK[i+j+1] = min(miniK[i+j+1],1+miniK[i-j])
                j+=1
            j = 1
            while i-(j-1)>=0 and i+j<len(s) and s[i-(j-1)] == s[i+j]:
                miniK[i+j+1] = min(miniK[i+j+1], 1+miniK[i-j+1])
                j+=1
        return miniK[len(s)]



sol = Solution()
print sol.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")    