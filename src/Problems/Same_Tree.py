'''
Created on 15 Jan 2015

@author: Yuan
'''
'''
Two trees are the same iff they have same val and the left and right are same, respectively.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None:
            if q == None:
                return True
            else:
                return False
        else:
            if q == None:
                return False
            else:
                return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        