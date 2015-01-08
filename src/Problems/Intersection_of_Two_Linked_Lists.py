'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
This problem can be solved with two pointers.
1. First connect the tail of one list to the head of another
2. If the two lists have intersection, then the connected list will contain a cycle. And the intersection begins where the cycle begins
3. Otherwise, the combined list will not have a cycle.
4. don't forget to detach the connection in step 1.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        tailB = headB
        while tailB.next != None:
            tailB = tailB.next
        tailB.next = headA
        slow = headB
        quick = headB
        while quick != None and quick.next != None:
            quick = quick.next.next
            slow = slow.next
            if slow == quick:
                quick = headB
                while quick != slow:
                    quick = quick.next
                    slow = slow.next
                tailB.next = None
                return slow
        tailB.next = None
        return None