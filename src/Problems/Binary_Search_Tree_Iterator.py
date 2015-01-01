'''
Created on 1 Jan 2015

@author: Yuan
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    
    stack = []
    
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.build(root)
    
    def build(self, root):
        node = root
        while node != None:
            self.stack.append(node)
            node = node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        self.build(node.right)
        return node.val        

# Your BSTIterator will be called like this:
root = TreeNode(5)
node3 = TreeNode(3)
root.left = node3
node1 = TreeNode(1)
node3.left = node1
node2 = TreeNode(2)
node1.right = node2
node4 = TreeNode(4)
node3.right = node4
node7 = TreeNode(7)
root.right = node7
node6 = TreeNode(6)
node7.left = node6

i, v = BSTIterator(root), []
# print i.hasNext()
# print i.next()
while i.hasNext(): 
    v.append(i.next())
for x in v:
    print x,