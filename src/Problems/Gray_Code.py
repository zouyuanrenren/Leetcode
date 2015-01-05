'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
There are rules about the digits
consider the following sequences of gray codes:
0        0000000    0    0
1        0000001    1    +1
2        0000011    3    +2
3        0000010    2    -1
4        0000110    6    +4
5        0000111    7    +1
6        0000101    5    -2
7        0000100    4    -1
8        0001100    12    +8
9        0001101    13    +1
10       0001111    15    +2
11       0001110    14    -1
12       0001010    10    -4
13       0001011    11    +1
14       0001001    9    -2
15       0001000    8    -1

Starting from right to left:
1. the first bit has a 0110 loop
2. the second bit has a 00111100 loop
3. the third bit has a 0000111111110000 loop
4. ...
so for each index i:
    for each digit x in range(n):
        the x digit == ((i + 2**x)/ 2**(x+1))%2
        in other word, the x digit corresponding to base = 2**x
        then result[i] += base*((i+base)/ (base*2))%2
'''
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return  [0]
        List = []
        for i in range(2 ** n):
            result = 0
            for x in range(n):
                base = 2 ** x
                result += base *(((i+base)/(base*2))%2)
            List.append(result)
        return List
    
    
list = Solution().grayCode(4)
for l in list:
    print l