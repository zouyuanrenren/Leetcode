'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
Given a singly linked list L: L0¡úL1¡ú¡­¡úLn-1¡úLn,
reorder it to: L0¡úLn¡úL1¡úLn-1¡úL2¡úLn-2¡ú¡­

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

'''
The basic idea is:
1. find out the length of the list;
2. take out and reverse the second half of the list;
3. merge the two lists.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        size = 0
        pointer = head
        if head == None:
            return None
        while pointer != None:
            size += 1
            pointer = pointer.next
        pointer = head
        if size == 1:
            return head
        for i in range((size-1)/2):
            pointer = pointer.next
        pre = pointer.next
        pointer.next = None
        pointer = pre
        pre = None
        while pointer != None:
            next = pointer.next
            pointer.next = pre
            pre = pointer
            pointer = next
        newpointer = head
        while pre:
            next1 = newpointer.next
            newpointer.next = pre
            next2 = pre.next
            pre.next = next1
            newpointer = next1
            pre = next2
