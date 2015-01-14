'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
This problem assumes a perfect binary tree, hence the problem can be solved by populating from root to leafs.
Particularly, for each non-leaf node:
    node.left.next = node.right
    node.right.next = node.next.left
    node = node.next
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            root.next = None
            row = root
            while row.left:
                node = row
                while node:
                    node.left.next = node.right
                    node.right.next = None if not node.next else node.next.left
                    node = node.next
                row = row.left