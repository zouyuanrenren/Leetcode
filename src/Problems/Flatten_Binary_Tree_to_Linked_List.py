'''
Created on 5 Jan 2015

@author: Yuan
'''

'''
A typical binary tree problem. 
It can be done by 
    1. first flatten the left-child, if exists, 
    2. and then append the end of current list with the flattened right-child, if exists
So a key-issue is to remember the end of the current list.
We consider the follow situations:
    1. a node has no left child
        i. if it has no right child either, the end is itslef
        ii. otherwise, flattend its right child, and the end is the end of its right child flattened.
    3. a node has left child:
        i. first flatten its left child, get the end, attach it to the right child position
        ii. if it has no right child, return the end
        iii. if it has a right child, flattend the right child, attach it to the current end, and return the new end
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None:
            return None
        self.flattenToEnd(root)
    
    def flattenToEnd(self,root):
        if root.left == None:
            if root.right == None:
                return root
            else:
                return self.flattenToEnd(root.right)
        else:
            end = self.flattenToEnd(root.left)
            right = root.right
            root.right = root.left
            root.left = None
            if right == None:
                return end
            else:
                end.right = right
                return self.flattenToEnd(right)

        