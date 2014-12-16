'''
Created on 21 Nov 2014

@author: zouyuanrenren
'''
'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''

'''
The idea is to use in-order traversal:
1. The in-order traversal of a BST is a list in ascending order;
2. If two elements are swapped, then the ascending order is broken;
3. There are two possibilities:
    a. the two elements are adjacent;
    b. the two elements are not adjacent;
4. in the first situation we find only one pair of val[i] > val[i+1]
   in the second stuation we find two pairs of val[i] > val[i+1] and val[j] >  val[j+1]
5. In the first situation, we swap back node[i] and node[i+1]
   I the second situaiton, we swap back node[i] and node[j+1]
'''


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    pre = None
    def recoverTree(self, root):
        self.pre = None
        pairs = []
        self.inorderTraversal(root, pairs)
        if len(pairs) == 2:
            pairs[0].val, pairs[1].val = pairs[1].val, pairs[0].val
        else:
            pairs[0].val, pairs[3].val = pairs[3].val, pairs[0].val
        return root
    
    def inorderTraversal(self, root, pairs):
        if root == None:
            return None
        self.inorderTraversal(root.left, pairs)
        if self.pre != None and root.val < self.pre.val:
            pairs.append(self.pre)
            pairs.append(root)
        self.pre = root
        self.inorderTraversal(root.right, pairs)
        
    
node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(2)
node1.right = node2
node2.left = node3

sol = Solution()
root = sol.recoverTree(node1)

def printTree(root):
    if root != None:
        printTree(root.left)
        print root.val,
        printTree(root.right)

printTree(root)
print

