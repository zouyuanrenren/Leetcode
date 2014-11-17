'''
Created on 16 Nov 2014

@author: zouyuanrenren
'''

'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 \leq m \leq n \leq length of list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None or m == n:
            return head
        result = ListNode(0)
        result.next = head
        pre = result
        for i in range(m-1):
            pre = pre.next
        newhead = pre.next
        newtail = pre.next
        current = newhead.next
        for i in range(m,n):
            newcurrent = current.next
            current.next = newhead
            newhead = current
            current = newcurrent
        newtail.next = current
        pre.next = newhead
        return result.next
    
list = [1,2,3,4,5]
head = ListNode(0)
tail = head
for item in list:
    tail.next = ListNode(item)
    tail = tail.next

sol = Solution()
head = sol.reverseBetween(head.next, 5,5)
while head != None:
    print head.val,
    head = head.next
print
        