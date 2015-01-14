'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
Very simple problem.
Remember to deal with the extra carry at the end of the loop.
'''
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 1
        for index in range(len(digits))[::-1]:
            digits[index] += carry
            carry = digits[index]/10
            digits[index] %= 10
        if carry == 1:
            digits = [1]+digits
        return digits
        