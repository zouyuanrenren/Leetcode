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
This question is relatively simple, just add the two numbers on each digit and add the carry to the next digit if needed.
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
        carry = 0
        while l1 != None or l2 != None or carry:
            if l1 != None:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0
            if l2 != None:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0
            val = n1 + n2 + carry
            newnode = ListNode(val % 10)
            current.next = newnode
            current = newnode
            carry = val / 10
        return result.next
    
list = [5,5,5]
head1 = ListNode(0)
tail = head1
for item in list:
    tail.next = ListNode(item)
    tail = tail.next
    
list = [5,5,5]
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

                    
            