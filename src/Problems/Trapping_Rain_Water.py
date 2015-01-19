'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
This problem has several solutions.
Solutoin1:
    1. find the peak of the array.
    2. for each bar to the left of the peak, if the tallest to its left is MAX, then it can hold MAX-bar water.
    3. for each bar to the right of the peak, if the tallest to its right is MAX, then it can hold MAX-bar water.

Solution2 is to use a stack. Need to add later.
'''
class Solution1:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        total = 0
        if len(A) == 0:
            return 0
        peak = 0
        for index in range(0, len(A)):
            if A[index] > A[peak]:
                peak = index
        pre = A[0]
        for index in range(0, peak):
            pre = max(pre, A[index])
            total += pre-A[index]
        pre = A[len(A)-1]
        index = len(A)-1
        while index > peak:
            pre = max(pre, A[index])
            total += pre-A[index]
            index -= 1
        return total
        