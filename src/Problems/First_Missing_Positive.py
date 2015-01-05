'''
Created on 1 Jan 2015

@author: Yuan
'''

'''
This problem requires O(n) time and O(1) extra space. We can make use of the original array to store intermediate results.
Particularly, in an array of size l, the first missing positive must be in [1, l+1]
Hence we can use A[i] to remember if i+1 appears in the array and A[i] = i+1 if it appears. (we can also make A[i] = True if i+1 appears)
At the end, if there is some A[i] != i+1, then we know that i+1 is missing.
    Otherwise, we know that i+2 = len(A)+1 is missing.
To do that we need to move elements around.
1. starting from the beginning of the list with pointer i
2. A[i] will be the current val to examine:
     a. if val is a postive in [1,l], then it should be put in A[val-1]. 
     b. If it is not already put there, then we need to assing val to A[val-1].
         i. In this case, the original A[val-1] becomes the new val.
         ii. go back to (a) and continue
         
Although there are two levels of loops (for-while), the complexity is still O(n), because:
1. every element will be moved at most once.
2. every element will be visited at most twice: once when i iterates through it, the other when the while-loop moves its value.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if len(A) == 0:
            return 1
        val = 0
        next = 0
        for i in range(0, len(A)):
            val = A[i]
            while val > 0 and val <= len(A) and A[val-1] != val:
                next = A[val-1]
                A[val-1] = val
                val = next
        for i in range(0, len(A)):
            if A[i] != i+1:
                return i+1
        return len(A)+1
        

print Solution().firstMissingPositive([1,-1,1,0,4])