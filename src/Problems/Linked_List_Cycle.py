'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

'''
Can be done with two pointers:
1. one fast pointer;
2. one slow pointer;
3. the list has a cycle iff fast == slow at some point
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast = head
        slow = head
        if head == None:
            return False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False   