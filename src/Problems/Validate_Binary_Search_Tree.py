'''
Created on 21 Nov 2014

@author: zouyuanrenren
'''

'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

'''
This can be easily solved with recursion. Given a node in the tree:
1. its left subtree should be less than the node;
    1.a if the node is a right child of its parent, its left-subtree should be greater than its parent;
2. its right subtree should be greater than the node;
    2.a if the node is a left child of its parent, its right-subtree should be less than its parent; 
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTMinMax(root, None, None)
    
    def isValidBSTMinMax(self, root, min, max):
        if root == None:
            return True
        if min != None and root.val <= min:
            return False
        if max != None and root.val >= max:
            return False
        return self.isValidBSTMinMax(root.left, min, root.val) and self.isValidBSTMinMax(root.right, root.val, max)


class Tree:
    root = None
    def __init__(self, x):
        nodes = []
        for val in x:
            if val == '#':
                nodes.append(None)
            else:
                nodes.append(TreeNode(val))
        for i in range(len(nodes)):
            if nodes[i] != None:
                left = 2*i+1
                right = 2*2+2
                if left < len(nodes):
                    nodes[i].left = nodes[left]
                if right < len(nodes):
                    nodes[i].right = nodes[right]
        if len(nodes)>0:
            self.root = nodes[0]

list = [2,1,3,'#','#',4,'#','#',5]
tree = Tree(list)
        
root = tree.root

sol = Solution()
print sol.isValidBST(root)