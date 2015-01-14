'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
This problem is similar to the Remove Duplicate from Sorted Array problem.
This can also be solved with two-pointer.
The difference is that, an element can be added into the result list when:
1. it is one of the first two elements.
2. it is different from the previous, or previous of previous of the slow pointed element.
'''
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A == None:
            return 0
        if len(A)<3:
            return len(A)
        fast = 2
        slow = 2
        while fast < len(A):
            if A[fast] != A[slow-1] or A[fast] != A[slow-2]:
                A[slow] = A[fast]
                slow+=1
            fast+=1
        return slow
    
A = [1,1,1,2,2,3]
print Solution().removeDuplicates(A)
print A