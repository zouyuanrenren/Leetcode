'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

'''
This problem can be solved by two-pointers.
The basic idea is that:
1. using a fast pointer to move k-steps;
2. if the fast pointer reaches the tail, link it to the head;
4. start the slow pointer k-steps later;
5. move the two pointers at the same time until the faster pointer reachers the tail, link it to the head;
6. break the link after the slow pointer and return the next node.
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
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        fast = head
        tail = None
        for i in range(k):
            if fast.next == None:
                tail = fast
                fast.next = head
            fast = fast.next
        slow = head
        while fast.next != tail:
            fast = fast.next
            slow = slow.next
        if fast.next == None:
            # this is the situation where fast is the actual tail
            fast.next = head
        else:
            # this is the situation where fast is one node before tail
            slow = slow.next
        newhead = slow.next
        slow.next = None
        return newhead
    
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
# node3.next = node4
# node4.next = node5

head = node1

sol = Solution()
newHead = sol.rotateRight(head, 2)

while newHead != None:
    print newHead.val,
    newHead = newHead.next
print
