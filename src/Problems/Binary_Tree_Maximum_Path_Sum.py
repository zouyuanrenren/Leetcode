'''
Created on 21 Nov 2014

@author: zouyuanrenren
'''
'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''

'''
The idea is simple:
1. for each node, there are 4 paths that include the node:
    a. node itself
    b. node + left sub-path with max sum
    c. node + right sub-path with max sum
    d. node + left sub-path with max sum + right sub-path with max sum
we only need to compute the largest out of the above 4 for each node
2. for each node, the sub-path with max sum that ends with the node can be:
    a. node itself
    b. node + left sub-path with max sum
    c. node + right sub-path with max sum
we only need to compute the largest out of the above 3 for each node, so that it can be used by its parent node
3. hence we do with depth-first search
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
    def maxPathSum(self, root):
        if root == None:
            return 0
        maxlist = []
        self.maxsum(root,maxlist)
        return max(maxlist)
        
    def maxsum(self,root,maxlist):
        if root == None:
            return 0
        leftmax = self.maxsum(root.left,maxlist)
        rightmax = self.maxsum(root.right,maxlist)
        result = max(root.val,root.val+leftmax,root.val+rightmax)
        current = max(result,root.val+leftmax+rightmax)
        maxlist.append(current)
        return result
