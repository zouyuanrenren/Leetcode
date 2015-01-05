'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
MAX(root) = 1+max(MAX(root.left), MAX(root.right))
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
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
        