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
        head = ListNode(0)
        pre = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1 == None:
            pre.next = l2
        else:
            pre.next = l1
        return head.next

l1 = ListNode(2)
l2 = ListNode(1)

sol = Solution()
result = sol.mergeTwoLists(l1, l2)
while result != None:
    print result.val
    result = result.next