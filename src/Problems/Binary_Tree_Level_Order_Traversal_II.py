'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
This problem is almost the same as Binary Tree Level Order Traversal
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        NodeList = []
        if root == None:
            return NodeList
        NodeList.append([root])
        level = 0
        while level < len(NodeList):
            newList = []
            for index in range(len(NodeList[level])):
                item = NodeList[level][index]
                if item.left != None:
                    newList.append(item.left)
                if item.right != None:
                    newList.append(item.right)
                NodeList[level][index] = item.val
            if len(newList) > 0:
                NodeList.append(newList)
            level += 1
        return NodeList[::-1]