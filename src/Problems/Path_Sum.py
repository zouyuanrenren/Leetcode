'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
A typical tree problem.
Note that only when the tree has no left nor right child, it is a leaf node.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if sum == root.val and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
