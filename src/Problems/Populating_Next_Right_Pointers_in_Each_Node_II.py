'''
Created on 14 Jan 2015

@author: Yuan
'''
'''
Similar as the Populating Next Right Pointers in Each Node, this problem can be solved from root to leaf.
Note that now the tree is not perfect, for each level of the tree we need to maintain following pointers:
1. the first node that has a child;
2. the first node that has a different child;
3. the first child on level+1;
2. the second child on level+1;

Then the following should be done:
1. first child.next = second child;
2. first child = second child;
3. first parent = second parent;
4. the second parent is the next node that has a different child;
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root != None:
            root.next = None
            level = root
            while level != None:
                firstParent = level
                # find the first parent
                while firstParent and not firstParent.left and not firstParent.right:
                    firstParent = firstParent.next
                firstChild = None
                # find the first child
                if firstParent:
                    if firstParent.left:
                        firstChild = firstParent.left
                    elif firstParent.right:
                        firstChild = firstParent.right
                level = firstChild
                while firstParent:
                    if firstChild and firstParent.right and firstChild != firstParent.right:
                        firstChild.next = firstParent.right
                        firstChild = firstChild.next
                    # find the next parent
                    secondParent = firstParent.next
                    while secondParent and not secondParent.left and not secondParent.right:
                        secondParent = secondParent.next
                    # connect first child to the child of second parent
                    if secondParent:
                        if secondParent.left:
                            firstChild.next = secondParent.left
                        elif secondParent.right:
                            firstChild.next = secondParent.right
                    firstChild = firstChild.next
                    firstParent = secondParent    

