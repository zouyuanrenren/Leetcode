'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
Recursion soltuion is trival.

An interative solution makes use of a stack and a list
1. push the root into stack
2. while the stack is non-empty, examine the top node:
    a. if the node has no right-child or its right-child = last poped node, pop itself and add to list
    b. else, push its right child into the stack

note that when push a node into the stack, one should push all the way down to its left-most off-spring
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
    def postorderTraversal(self, root):
        List = []
        stack = []
        lastPoped = None
        self.push(stack, root)
        while stack:
            node = stack[-1]
            if node.right == None or node.right == lastPoped:
                lastPoped = stack.pop()
                List.append(node.val)
            else:
                self.push(stack, node.right)
        return List
    
    def push(self, stack, node):
        while node != None:
            stack.append(node)
            node = node.left