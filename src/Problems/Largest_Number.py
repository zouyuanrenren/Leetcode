'''
Created on 13 Jan 2015

@author: Yuan
'''
'''
This problem is essentially a sorting problem:
Sort all the numbers w.r.t. their first digits, if the same then w.r.t. the second digits, so on and on.

The tricky case is when two numbers X and Y have the same prefix, but one is shorter than the other.
In this case, X is smaller than Y when X+y is smaller than Y + X.
Another corner case is when the results containing many leading "0", in this case return "0".
'''

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda x,y:cmp(y+x, x+y))
        return "".join(num).lstrip("0") or "0"
        
sol = Solution()
print sol.largestNumber([1,2,2,2,23,2,3])
