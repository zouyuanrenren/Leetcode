'''
Created on 16 Nov 2014

@author: zouyuanrenren
'''

'''
Sort a linked list using insertion sort.

The basic idea is:
1. use a tail-current pair to separate the sorted and unsorted part of the list;
2. if current >= tail, then move on to the next node
3. else, need to insert current into head ->...-> tail part
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
        
        newhead = ListNode(0)
        newhead.next = head
        tail = head
        current = head.next
        while current != None:
            if current.val < tail.val:
                pre = newhead
#                 if pre.next != None and pre.next.val > current.val:
#                     pre = newhead
                while pre.next.val < current.val:
                    pre = pre.next
                newcurrent = current.next
                current.next = pre.next
                pre.next = current
                current = newcurrent
                tail.next = current
            else:
                tail = current
                current = current.next
        return newhead.next
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node22 = ListNode(2)

node2.next = node1
node1.next = node3
node3.next = node22

head = node2

sol = Solution()
newHead = sol.insertionSortList(head)

while newHead != None:
    print newHead.val,
    newHead = newHead.next
print