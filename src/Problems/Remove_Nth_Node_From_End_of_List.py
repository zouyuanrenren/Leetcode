'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

'''
The basic idea is:
1. use two-pointers with distance n+1;
2. when the fast pointer reaches None, the slow pointer should reach the node before the nth node from the end;
3. remove the next node of the slow pointer.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):        
        if n == 0:
            return head
        result = ListNode(0)
        result.next = head
        fast = result
        slow = result
        while n+1>0:
            fast = fast.next
            n -= 1
        while fast != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return result.next
    
list = [1,2,3,4,5]
head = ListNode(0)
tail = head
for item in list:
    tail.next = ListNode(item)
    tail = tail.next
    
sol = Solution()
head = sol.removeNthFromEnd(head.next, 2)

while head != None:
    print head.val,
    head = head.next
print
        