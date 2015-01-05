'''
Created on 1 Jan 2015

@author: Yuan
'''
'''
This problems requies O(1) time for next() and hasNext(). This requires the tree to be serialised in-order.
This can be done with a stack and a list:
1. push the root into the stack
2. while the stack is non-empty, pop the top element, add it into the list, and push its right sub-tree node into the stack

Note that, when push a node into stack, one should push all the way down to its left-most sibling nodes

by doing the above, the list will be a in-order serialisation of the tree
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.list = []
        self.pointer = 0
        self.build(root)
    
    def build(self, root):
        self.push(root)
        while self.stack:
            node = self.stack.pop()            
            self.list.append(node.val)
            self.push(node.right)
    
    def push(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.pointer < len(self.list)

    # @return an integer, the next smallest number
    def next(self):
        if self.pointer < len(self.list):
            val = self.list[self.pointer]
            self.pointer +=1
            return val        

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