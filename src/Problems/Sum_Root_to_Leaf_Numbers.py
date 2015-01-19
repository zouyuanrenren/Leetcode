'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
This is a depth first search problem.
For each node, the "partial path sum up to the current point" is "partial path sum up to its parent" * 10 + node.val
    for the root node, the partial path sum up to its parent = 0
If the node has no child, add the current partial path sum to the final result
If it has a left child, compute the total sum for the left child first.
If it has a right child, compute the total sum for the right child then.
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
    def sumNumbers(self, root):
        if root == None:
            return 0
        return self.sumSoFar(root,0,0)
    
    def sumSoFar(self,root,total,pre):
        if root.left == None:
            if root.right == None:
                return total+pre*10+root.val
            else:
                return self.sumSoFar(root.right, total,(pre*10+root.val))
        elif root.right == None:
            return self.sumSoFar(root.left, total, (pre*10+root.val))
        else:
            total = self.sumSoFar(root.left, total, (pre*10+root.val))
            return self.sumSoFar(root.right, total,(pre*10+root.val))
        