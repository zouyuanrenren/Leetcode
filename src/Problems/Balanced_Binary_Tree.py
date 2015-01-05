'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
a tree is a balanced binary tree if its abs(left.depth - right.depth) <= 1 and left and right are both balanced binary tree
hence this is a depth-first search problem that can be solved with recursion

An alternative solution 2 is to combine the BBT testing with depth computation. So that no redundant tree traversal is needed.
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
    def isBalanced(self, root):
        if root == None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.depth(root.left)-self.depth(root.right)) <= 1
    def depth(self,root):
        if root == None:
            return 0
        return 1+max(self.depth(root.left), self.depth(root.right))
 
class Solution2:
    # @param root, a tree node
    # @return an integer
    def isBalanced(self, root):
        return self.testBBT(root, [0])
    
    def testBBT(self, root, depth):
        if root  == None:
            depth[0] = 0
            return True
        ldepth = [0]
        lBBT = self.testBBT(root.left, ldepth)
        rdepth = [0]
        rBBT = self.testBBT(root.right, rdepth)
        rootBBT = lBBT and rBBT and abs(ldepth[0]-rdepth[0]) <= 1
        depth[0] = max(ldepth[0],rdepth[0])+1
        return rootBBT
