'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
Similar as the Single Number problem. One can use either a hash table solution or a bit manipulation solution.
1. The hash table solution essentially count the appearances of numbers.
    In the following Solution1, we count the appearances of numbers on each digit.
    Nevertheless, this solution requires non-constant space.
    
2. The bit manipulation solution attempts to find which bit has 1 appearance such that appearance % 3 != 0.
    To do this we use a number ex1 to record if each bit has 1 appearance such that appearance % 3 >= 1
    and use ex2 to record if each bit has 1 appearance such that appearance % 3 = 2.
    Final results would be ex1.
    And the calculation of ex1 and ex2 for each digit is as follows:
    ex1    ex2    input    ex1    ex2
    0        0        0    0        0
    0        0        1    1        0
    1        0        0    1        0
    1        0        1    1        1
    1        1        0    1        1
    1        1        1    0        0
    
    From the above truth value table, we can derive that 
    ex1 = ~ex1 & ~ex2 & input | ex1 & ~ex2 & ~input | ex1 & ~ex2 & input | ex1 & ex2 & ~input
    = ex1 & (ex2 ^ input) | ~ex2 & (ex1 ^ input)
    ex2 = ex1 & (ex2 ^ input)
    In the following Solution2, we use this solution.
    This solution requires constant space.
'''
class Solution1:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # we make a counter for negative numbers
        counter = 0
        # we make a 10 * 10 table to maintain the counters for each number on each digit
        # each row is a digit
        # each col is a num
        counters = []
        for i in range(10):
            counters.append([0]*10)
        for item in A:
            if item < 0:
                counter += 1
            digit = 9
            Num = abs(item)
            while digit >= 0:
                offset = 10 ** digit
                counters[9-digit][(Num/offset)]+=1
                Num %= offset
                digit -= 1
        result = 0
        for row in counters:
            result *= 10
            for index,col in enumerate(row):
                if col%3 != 0:
                    result += index
                    break
        if counter %3 != 0:
            result = 0- result
        return result
    
class Solution2:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ex1 = 0
        ex2 = 0
        for input in A:
            nex1 = ex1 & (ex2 ^ input) | ~ex2 & (ex1 ^ input)
            ex2 = ex1 & (ex2 ^ input)
            ex1 = nex1
        return ex1

print Solution2().singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])