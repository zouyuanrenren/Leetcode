'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
A depth-first search problem, pass the current path down to children nodes to find the root-leaf path.
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
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        List = []
        if root == None:
            return List
        current = []
        self.getPathSum(List,current,root,sum)
        return List
        
    def getPathSum(self,List,current,root,sum):        
        if sum == root.val and root.left == None and root.right == None:
            current.append(root.val)
            List.append(current)
        else:
            if root.left != None:
                newcurrent = current[:]
                newcurrent.append(root.val)
                self.getPathSum(List, newcurrent, root.left, sum-root.val)
            if root.right != None:
                newcurrent2 = current[:]
                newcurrent2.append(root.val)
                self.getPathSum(List, newcurrent2, root.right, sum-root.val)