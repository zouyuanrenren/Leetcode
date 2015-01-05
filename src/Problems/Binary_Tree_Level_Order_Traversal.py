'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
This problem is a typical breadth-first-search problem.
It can be solved with a two level queues NodeList[][]
Nodelist[i][j] is the j-th node on the i-the level of the tree
Children of NodeList[i][j] will be added into NodeList[i+1]
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
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
        return NodeList
        