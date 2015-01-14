'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
This problem requires constant space consumption, hence we cannot convert the int to string.
A straight-forward solution is as follows:
1. compare the first and last digit. 
    a. If not same, return true
    b. If the same, remove the first and last digits, repeat 1.
Since the range of int is -2,147,483,648 to 2,147,483,647, then the base of the first digit is no higher than 1,000,000,000.
We can start from 1,000,000,000 to find the base for the first digit.
'''
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        base = 1000000000
        while x < base:
            base /= 10
        while base > 1:
            if x / base != x % 10:
                return False
            x %= base
            x /= 10
            base /= 100
        return True
