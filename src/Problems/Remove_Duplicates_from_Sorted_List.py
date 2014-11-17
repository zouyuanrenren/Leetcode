'''
Created on 16 Nov 2014

@author: zouyuanrenren
'''
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

'''
The basic idea is:
1. going through nodes one by one:
2. if a node has the same value as its next node, skip the next node;
3. otherwise, proceeds; 
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        current = head
        if current != None:
            next = current.next
            while next != None:
                if current.val == next.val:
                    current.next = next.next
                    next = next.next
                else:
                    current = next
                    next = next.next
        return head
        