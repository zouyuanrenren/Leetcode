'''
Created on 1 Jan 2015

@author: Yuan
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