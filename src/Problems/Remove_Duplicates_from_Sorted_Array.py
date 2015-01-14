'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
This problem basically ask for the number of unique elements in list A.
Note that A is sorted.
An element is unique only if:
    a. it is the first element.
    b. it is different from its previous element.
Then the problme can be solved with two-pointer:
    a. a fast pointer points to the next element.
    b. a slow pointer points to the next position for unique element.
'''
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == None:
            return 0
        if len(A) < 2:
            return len(A)
        slow = 1
        fast = 1
        while fast < len(A):
            if A[fast] != A[fast-1]:
                A[slow] = A[fast]
                slow += 1
            fast += 1
        return slow
        