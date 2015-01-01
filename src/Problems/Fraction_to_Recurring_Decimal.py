'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        symbol = True
        if numerator * denominator < 0:
            symbol = False
        numerator = abs(numerator)
        denominator  = abs(denominator)    
        numer = [numerator]
        numerator %= denominator
        numerator *= 10
        repeat = -1
        result = ""
        while numerator != 0:
            if numerator in numer:
                repeat = numer.index(numerator)
                break;
            numer.append(numerator)
            numerator = numerator % denominator
            numerator *= 10
        if symbol == False:
            result +="-"
        result += str(numer[0]/denominator)
        if len(numer) > 1:
            result+="."
        for i in range(1, len(numer)):
            div = numer[i]/denominator
            if repeat == i:
                result +="("
            result+=str(div)
        if repeat != -1:
            result+=")"
        return result

print Solution().fractionToDecimal(50,-8)
