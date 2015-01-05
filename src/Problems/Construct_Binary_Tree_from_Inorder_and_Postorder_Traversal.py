'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
This problem can be solved with recursion.
Assuming we have the following two lists:

inorder:     .................l|t|r...................
postorder:   .................m|s...................|t

Obviously, t is the root node, then:
1. the [...l] part in the inorder list is the left sub-tree, it corresponds to the [...m] part in the postorder list
2. the [r...] part in the inroder list is the right sub-tree, it corresponds to the [s...] part in the postorder list

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
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.buildFrom2Lists(inorder, 0, postorder, 0, len(postorder))
    
    def buildFrom2Lists(self,inorder, istart, postrorder, pstart, length):
        if length == 0:
            return None
        if length == 1:
            return TreeNode(inorder[istart])
        root = TreeNode(postrorder[pstart+length-1])
        index = inorder[istart:istart+length].index(root.val)+istart
        root.left = self.buildFrom2Lists(inorder, istart, postrorder, pstart, index-istart)
        root.right = self.buildFrom2Lists(inorder, index+1, postrorder, pstart+index-istart, istart+length-index-1)
        return root