'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
The results consists of several parts:
1. the symbol
2. the part before "."
3. the non-recurring part after "."
4. the recurring part after "."

They need different treatments:
1. iff the numerator and denomiantor have differet symbols, then final symbol = "-"
2. update the numerator and denominator with their abstract values.
3. the part before "." is the original numerator/denominator
4. recursively perform the following:
    i. update numerator = (numbertor%denominator)*10
    ii. if a numerator re-occurs, then repeating is found, stop the recursion
    iii. otherwise, remember it in a list
5. if the list of remembered numerator > 0, then we append a "."
6. the results then should be appended with each remembered numerator/denominator
    i. if there is a repeat, we add ( before appending the result
7. if there is a repeat, we add ) after all results
'''
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        result = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator  = abs(denominator) 
        result+=str(numerator/denominator)
        numer = []
        numerator = (numerator%denominator)*10
        repeat = -1
        while numerator != 0:
            if numerator in numer:
                repeat = numer.index(numerator)
                break;
            numer.append(numerator)
            numerator = (numerator%denominator)*10
        if len(numer) > 0:
            result+="."
        for i in range(0, len(numer)):
            if repeat == i:
                result +="("
            result+=str(numer[i]/denominator)
        if repeat != -1:
            result+=")"
        return result

print Solution().fractionToDecimal(10,-7)
