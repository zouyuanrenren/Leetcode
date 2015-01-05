'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
A binary search problem:
Given a sorted array:
    1. the root will be the mid node. 
    2. The left sub-array should be converted into the left sub-tree;
    3. the right sub-array should be converted into the right sub-tree;
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.createTree(num,0,len(num))
    def createTree(self,num,start,end):
        if start == end:
            return None
        if start == end-1:
            return TreeNode(num[start])
        mid = start+(end-start)/2
        root = TreeNode(num[mid])
        root.left = self.createTree(num, start, mid)
        root.right = self.createTree(num, mid+1, end)
        return root
        