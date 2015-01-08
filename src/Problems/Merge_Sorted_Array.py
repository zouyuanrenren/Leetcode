'''
Created on 8 Jan 2015

@author: Yuan
'''
'''
This merge can be performed in place.
Starting from the end of the lists to the beginning of the lists.
This make sures that no original element will be overwritten.
'''
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        Aindex = m-1
        Bindex = n-1
        Allindex = m+n
        while Aindex >= 0 and Bindex >= 0:
            Allindex -= 1
            if A[Aindex] >= B[Bindex]:
                A[Allindex] = A[Aindex]
                Aindex -= 1
            else:
                A[Allindex] = B[Bindex]
                Bindex -= 1
        if Aindex < 0:
            for i in range(Allindex):
                A[i] = B[i]