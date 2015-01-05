'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
This problem can be solved with recursion.
Assuming we have the following two lists:

inorder:     .................l|t|r...................
preorder:    t/m.................|s...................

Obviously, t is the root node, then:
1. the [...l] part in the inorder list is the left sub-tree, it corresponds to the [m...] part in the preorder list
2. the [r...] part in the inroder list is the right sub-tree, it corresponds to the [s...] part in the preorder list

Hence, we can recursively generate the two sub-trees from sub-lists

In this algorithm, other key parameters include the starting position in two lists, and the length of lists to be matched.
Initially, they are 0, 0  and len(inorder)

'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.buildFrom2Lists(preorder, 0, inorder, 0, len(preorder))
    
    def buildFrom2Lists(self,preorder, pstart, inorder, istart, length):
        if length == 0:
            return None
        if length == 1:
            return TreeNode(preorder[pstart])
        root = TreeNode(preorder[pstart])
        index = inorder[istart:istart+length].index(root.val)+istart
        root.left = self.buildFrom2Lists(preorder, pstart+1, inorder, istart, index-istart)
        root.right = self.buildFrom2Lists(preorder, pstart+(index-istart)+1, inorder, index+1, istart+length-index-1)
        return root