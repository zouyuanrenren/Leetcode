'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
The multiplication of two numbers can be computed by multiplying each pair of digits.
Note that for the i-th digit in num2 and j-th digit in num1, the result should be on the (i+j)-th digit of the final results.
Hence result[i+j] should be updated as carry + num2[i]*num1[j]+carry.
'''
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        carry = 0
        if len(num1) == 1 and num1[0] == "0" or len(num2) == 1 and num2[0] == "0":
            return "0"
        result = ["0"]*(len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num2)):
            carry = 0
            for j in range(len(num1)):
                sum=carry+int(num2[i])*int(num1[j])+int(result[i+j])
                result[i+j] = str(sum%10)
                carry = sum/10
            if carry > 0:
                sum = carry+int(result[i+len(num1)])
                result[i+len(num1)] = str(sum)
        if carry > 0:
            result[len(num1)+len(num2)-1] = str(carry)
        else:
            result.pop()
        return "".join(result[::-1])
                


sol = Solution()
print sol.multiply("9369162965141127216164882458728854782080715827760307787224298083754", "7204554941577564438")