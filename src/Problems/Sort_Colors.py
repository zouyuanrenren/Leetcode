'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
This problem can be solved in place by using 2/3-pointers.
We maintain the pointer for the next 0 to fill, and the pointer for the next 1 to fill,
and of course the pointer for the next 2 to fill.
When a 0 is encountered:
    we fill it into the next 0 pointer, and fill the original value on next 0 to next 1, and fill the original value on next 1 to the next 2
when a 1 is encountered:
    we fill it into th next 1 pointer, and fill the original value on next 1 to next 2.
And we move the pointers forward accordingly.
'''
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A == None or len(A) == 0:
            return A
        next0 = 0
        next1 = 0
        for next in range(0,len(A)):
            if A[next] == 0:
                A[next] = A[next1]
                A[next1] = 1
                A[next0] = 0
                next0 += 1
                next1 += 1
            elif A[next] == 1:
                A[next] = A[next1]
                A[next1] = 1
                next1+=1
        return A