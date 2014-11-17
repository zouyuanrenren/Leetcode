'''
Created on 16 Nov 2014

@author: zouyuanrenren
'''

'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

the basic idea is to construct the tree in an bottom-up manner
the tree can be constructed with inorder search
when the size of the tree is known, one always knows how many nodes need to be processed to build a sub-tree
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    current = ListNode(0)
    def sortedListToBST(self, head):
        if head == None:
            return None
        size = 0
        p = head
        while p != None:
            size += 1
            p = p.next
        
        self.current = head
        return self.generateBST(size)
    
    def generateBST(self, size):
        if size == 0:
            return None
        leftchild = self.generateBST(size/2)
        root = TreeNode(self.current.val)
        root.left = leftchild
        self.current = self.current.next
        root.right = self.generateBST(size - (size/2) - 1)
        return root

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()

root = sol.sortedListToBST(node1)

def inorder(root):
    if root != None:
        inorder(root.left)
        print root.val,
        inorder(root.right)

inorder(root)
print
