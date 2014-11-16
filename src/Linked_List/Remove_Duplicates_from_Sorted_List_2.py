'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

'''
The basic idea is to add only node that is different from its previous one and different from its next one:
1. add a temp node before head with a different value from head
2. for each node, if it is the same as its previous node, then skip
3. otherwise, if it has a next node and has the same value, then skip
4. otherwise
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        tail = ListNode(head.val-1)
        tail.next = head
        newhead = tail
        
        pre = tail
        while head != None:
            if head.val == pre.val:
                pre = head
                head = head.next
            elif head.next != None and head.next.val == head.val:
                pre = head
                head = head.next
            else:
                tail.next = head
                tail = head
                head = head.next
                pre = tail             
        
        tail.next = None
        return newhead.next
    
list = [1,1,2,2,3,3,4,4,4,5]
head = ListNode(0)
tail = head
for item in list:
    tail.next = ListNode(item)
    tail = tail.next

sol = Solution()
head = sol.deleteDuplicates(head.next)
while head != None:
    print head.val,
    head = head.next
print