'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

'''
The basic idea is to use two pointers:
1. one < pointer
2. one >= pointer
3. append nodes correspondingly to these two pointers
4. cut the end of the >= pointer
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        lessHead = ListNode(0)
        moreHead = ListNode(0)
        lessCurrent = lessHead
        moreCurrent = moreHead
        current = head
        while current != None:
            if current.val < x:
                lessCurrent.next = current
                lessCurrent = current
            else:
                moreCurrent.next = current
                moreCurrent = current            
            current = current.next
        lessCurrent.next = moreHead.next
        moreCurrent.next = None
        return lessHead.next
    
list = [2,1]
head = ListNode(0)
tail = head
for item in list:
    tail.next = ListNode(item)
    tail = tail.next

sol = Solution()
head = sol.partition(head.next,2)
while head != None:
    print head.val,
    head = head.next
print