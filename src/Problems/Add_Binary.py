'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
basic idea is to obtain the last bits of each string, and add it to a carry initially  = False
if a string is empty, its last bit is False
so, result += (A != B) != Carry
and Carry = (A and B) or (A and Carry) or (B and Carry)
remember to take care of the last carry
'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        carry = False
        result = ""
        while a != "" or b != "":
            if a != "":
                A = a[-1] == '1'
                a = a[:len(a)-1]      
            else:
                A = False
            if b != "":
                B = b[-1] == '1'
                b = b[:len(b)-1]
            else:
                B = False
            if (A != B) != carry:
                result += '1'
            else:
                result += '0'
            carry = (A and B) or (A and carry) or (B and carry)
        if carry:
            result += '1'
        return result[::-1]