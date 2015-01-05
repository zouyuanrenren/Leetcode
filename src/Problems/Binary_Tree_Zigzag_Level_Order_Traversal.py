'''
Created on 4 Jan 2015

@author: Yuan
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Not much different from Binary Tree Level Order Traversal.
Only difference is to reverse the order of list with level%2
'''
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
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
        for level in range(len(NodeList)):
            if level % 2 == 1:
                NodeList[level] = NodeList[level][::-1]
        return NodeList