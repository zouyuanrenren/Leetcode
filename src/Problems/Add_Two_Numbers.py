'''
Created on 16 Nov 2014

@author: zouyuanrenren
'''

'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

'''
This question is relatively simple, just add the two numbers on each digit and add the addional 1 to the next digit if needed.
Need to be careful when one of the list ends before the other.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        current = result
        add = 0
        while l1 != None and l2 != None:
            val = l1.val + l2.val +add            
            newnode = ListNode(val % 10)
            current.next = newnode
            current = newnode
            add = val / 10
            l1 = l1.next
            l2 = l2.next
        leftover = None
        if l1 == None:
            if l2 != None:
                leftover = l2
        else:
            leftover = l1
        while leftover != None:
            val = leftover.val + add
            newnode = ListNode(val % 10)
            current.next = newnode
            current = newnode
            add = val / 10
            leftover = leftover.next
        if add == 1:
            newnode = ListNode(1)
            current.next = newnode
        return result.next
    
list = [1]
head1 = ListNode(0)
tail = head1
for item in list:
    tail.next = ListNode(item)
    tail = tail.next
    
list = [9,9,9]
head2 = ListNode(0)
tail = head2
for item in list:
    tail.next = ListNode(item)
    tail = tail.next
    
sol = Solution()
result = sol.addTwoNumbers(head1.next, head2.next)
while result != None:
    print result.val,
    result = result.next

                    
            