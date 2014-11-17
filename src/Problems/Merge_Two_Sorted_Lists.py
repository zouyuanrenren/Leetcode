'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

'''
A simpler case of the Merge_k_Sorted_List

The basic idea is:

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        else:
            if l2 == None:
                return l1
            else:
                head = None
                current = None
                if l1.val < l2.val:
                    head = l1
                    current = l2
                else:
                    head = l2
                    current = l1
                pre = head
                while pre.next != None and current != None:
                    if pre.next.val < current.val:
                        pre = pre.next
                    else:
                        next = pre.next
                        pre.next = current
                        pre = current
                        current = next
                else:
                    if pre.next == None:
                        pre.next = current
            return head