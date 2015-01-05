'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
This problem has two solutions.

Solution 1 is recursion:
1. maintain a list of elements
2. for each node, first recursively traverse its left sub-tree and add to the list
3. then append the list with the node value.
3. then recursively traverse its right sub-tree and add to the list

Solution 2 is iteration:
using a stack and a list
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        List = []
        current  = root
        if current == None:
            return List
        self.pushStack(stack, current)
        while len(stack) != 0:
            current = stack.pop()
            List.append(current.val)
            if current.right != None:
                self.pushStack(stack,current.right)
        return List
    def pushStack(self,stack, root):
        while root != None:
            stack.append(root)
            root = root.left