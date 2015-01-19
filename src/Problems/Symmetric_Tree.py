'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
This problem can have a few different solutions:
1. Solution1 is to reduce it to a two-tree-comparison problem.
    a. root is a symmetric tree if root.left is symmetric to root.right.
    b. a left tree is symmetric to a right tree iff:
        i. left = right = None 
        ii. or left.val = right.val and left.left is symmetric to right.right and left.right is symmetric to right.left
        
2. Solution2 is to do it in an iterative manner:
    a. using a stackL to maintain the left
    b. using a stackR to maintain the right
    c. perform symmetric operations to stackL and stackR:
        i. when pop, check if both pop the same value;
        ii. when push left child in stackL, push right child in stackR;
        iii. when push right child in stackL, push left child in stackR;
        iv. two stacks should have the same size
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.isSymmetric2(root.left, root.right)
    def isSymmetric2(self, node1, node2):
        if node1 == None:
            if node2 == None:
                return True
            else:
                return False
        else:
            if node2 == None:
                return False
            else:
                return node1.val == node2.val and self.isSymmetric2(node1.left, node2.right) and self.isSymmetric2(node2.left, node1.right)
            
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        stackL = []
        stackR = []
        self.pushL(stackL, root.left)
        self.pushR(stackR, root.right)
        while stackL and len(stackL) == len(stackR):
            l = stackL.pop()
            r = stackR.pop()
            if l.val == r.val:
                self.pushL(stackL,l.right)
                self.pushR(stackR,r.left)
            else:
                return False
        if stackL or stackR:
            return False
        return True
    
    def pushL(self, stack, node):
        while node:
            stack.append(node)
            node = node.left
            
    def pushR(self, stack, node):
        while node:
            stack.append(node)
            node = node.right
