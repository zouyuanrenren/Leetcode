'''
Created on 9 Jan 2015

@author: Yuan
'''

'''
Typical tree problem.
Solved with depth-first search. Implemented with recursion.
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None:
            if root.right == None:
                return 1
            else:
                return 1+self.minDepth(root.right)
        else:
            if root.right == None:
                return 1+ self.minDepth(root.left)
            else:
                return 1+min(self.minDepth(root.left),self.minDepth(root.right))