'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
A typical two-pointer problem.
There can be several solutions.

Solution1 uses swap:
A head pointer points to the next position to look into.
A tail pointer points to the next element that can be used to replace elem.
Solution1 is unstable


Solution2:
A fast pointer points to the next element to investigate
A slow pointer points to the next position to put an element.
Solution2 is stable
'''
class Solution1:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        head = 0
        tail = len(A)-1
        while head <= tail:
            if A[head] == elem:
                if A[tail] != elem:
                    A[head] = A[tail]
                tail -= 1
            else:
                head += 1
        return tail+1
    
class Solution2:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        fast = 0
        slow = 0
        while fast < len(A):
            if A[fast] != elem:
                A[slow] = A[fast]
                slow += 1
            fast += 1
        return slow
