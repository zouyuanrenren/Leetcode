'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

'''
The basic idea is to keep reversing the next at most k nodes. If it ends before k nodes are reversed, reverse the last batch
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head == None or head.next == None:
            return head
        newhead = ListNode(0)
        pre = newhead
        newhead.next = head
        num = k
        current = None
        while head != None:
            nexthead = head.next
            head.next = current
            current = head
            head = nexthead
            if num == k:
                tail = current
            num -= 1
            if num == 0:
                num = k
                pre.next = current
                pre = tail
                current = None
        if num > 0:
            head = current
            current = None
            while head != None:
                nexthead = head.next
                head.next = current
                current = head
                head = nexthead
            pre.next = current
        return newhead.next

list = [1,2,3,4,5]
head = ListNode(0)
tail = head
for item in list:
    tail.next = ListNode(item)
    tail = tail.next

sol = Solution()
head = sol.reverseKGroup(head.next, 2)
while head != None:
    print head.val,
    head = head.next
print