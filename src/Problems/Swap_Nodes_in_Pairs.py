'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

'''
This is a special case of Reverse_Nodes_in_k-Group.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        newhead = ListNode(0)
        newhead.next = head
        tail = newhead
        current = head
        while current != None and current.next != None:
            swap = current.next
            current.next = swap.next
            swap.next = current
            tail.next = swap
            tail = current
            current = current.next
        return newhead.next