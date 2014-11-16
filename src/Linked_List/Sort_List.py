'''
 Sort a linked list in O(n log n) time using constant space complexity.
'''

'''
This problem can be solved by quick-sort or merge-sort

using merge-sort, the idea is:
1. using fast-slow pointers to find the middle node;
2. recursively merge-sort the part before and after the middle node;
3. merge the two sorted sub-lists
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    
    # this solution uses the merge sort
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        # find the middle node
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        fast = slow
        slow = slow.next
        fast.next = None
        # sort the first and second halves
        fast = self.sortList(head)
        slow = self.sortList(slow)
        #         merge the sorted lists
        return self.merge(fast, slow)
    
    def merge(self,head1,head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        sorted = None
        if head1.val < head2.val:
            sorted = head1
            head1 = head1.next
        else:
            sorted = head2
            head2 = head2.next
        tail = sorted
        while head1 != None and head2 != None:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1 == None:
            tail.next = head2
        elif head2 == None:
            tail.next = head1
        return sorted
            
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node22 = ListNode(2)

node2.next = node1
node1.next = node3
node3.next = node22

head = node2

sol = Solution()
newHead = sol.sortList(head)

while newHead != None:
    print newHead.val,
    newHead = newHead.next
print
