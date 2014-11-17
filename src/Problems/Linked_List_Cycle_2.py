'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
'''

'''
Basic idea is to use two pointers:
1. a fast pointer;
2. a slow pointer:
3. when the two pointer meets, the head-2-slow distance = slow-2-cycle-begin-node distance
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast = head
        slow = head
        if head == None:
            return None
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head       
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None 