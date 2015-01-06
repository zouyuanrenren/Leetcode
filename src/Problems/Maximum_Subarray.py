'''
Created on 6 Jan 2015

@author: Yuan
'''
'''
This problem can be solved with dynamic programming.
Let us use Max[i] to represent the sum of maximum subarray ends with A[i].
Obvious the following holds:
    1. Max[0] = A[0]
    2. for i > 0, if Max[i-1]+A[i] < A[i], then Max[i] = A[i].
        this can be proved with controposition:
        a. assume Max[i] != A[i] but A[i] + m, obviously m > 0
        b. from assumption there is a subarray S ending of A[i-1], s.t. sum[S] = m
        c. from Max[i-1]+A[i] < A[i], we have Max[i-1] < 0
        d. combine a,b and c we can see that S, who ends with A[i-1] has a larger sum than Max[i-1], this is a contradiction.
        Hence we proved point 2.

Following the above idea, we can solve the problem with dynamic programming.
Note that to compute Max[i] we only need Max[i-1], hence we only need to maintian the previous maximum subarray sum.
So we can use a single variable to maintain the sum of maximum subarray that ends at the previous point.


A divide and conqurer solution is also available.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0:
            return 0
        Max = A[0]
        Sum = A[0]
        for item in A[1:]:
            Sum = max(Sum+item, item)
            Max = max(Sum,Max)
        return Max