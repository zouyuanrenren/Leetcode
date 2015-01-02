'''
Created on 2 Jan 2015

@author: Yuan
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
#             sum = carry
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