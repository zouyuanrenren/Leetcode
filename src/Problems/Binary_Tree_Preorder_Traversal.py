'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
Recursive solution is trivial.
An iterative solution can be developed by using a stack and a list:
1. push the root into the stack
2. when the stack is non-empty, pop the top element and push its left child into the stack

Note that, when pushing a node into stack, one should also append its value into the list
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        stack = []
        list = []
        self.push(stack, list, root)
        while stack:
            node = stack.pop()
            self.push(stack, list, node.right)
        return list
            
    def push(self, stack, list, node):
        while node != None:
            list.append(node.val)
            stack.append(node)
            node = node.left
            