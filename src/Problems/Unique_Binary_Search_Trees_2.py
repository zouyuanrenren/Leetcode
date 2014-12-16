'''
Created on 21 Nov 2014

@author: zouyuanrenren
'''
'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
'''

'''
This problem can be solved with dynamic programming:
1. given a number n;
2. a BST of n with size n can have root value m in [1, n];
3. for a root value m, its left sub-tree is a BST of m-1 with size m-1;
4. for a root value n, its right sub-tree is a BST of n with size n-m;

To do this, we leverage the following data structures:
1. lists is a (n+1)*(n+1) matrix, lists[x][y] maintains the list of all possible BSTs of size = x and max = y
2. we construct the lists[i][i] with increasing i
    a. the left child can be select from lists[m][m] with m < i
    b. the right child can be select from lists[i-m-1][i]
3. once a list for lists[i][i] is construct, we populate the i-row of lists by increasing the value of each BST in lists[i][i]
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        lists = []
        for x in range(n+1):
            lists.append([])
            for y in range(n+1):
                lists[x].append([]) 
        for y in range(n+1):
            lists[0][y].append(None)
            
        for i in range(1,n+1):
            for m in range(i):
                for leftindex in range(len(lists[m][m])):
                    leftchild = lists[m][m][leftindex]
                    l = i-m-1
                    for rightindex in range(len(lists[l][i])):
                        rightchild = lists[l][i][rightindex]
                        root = TreeNode(m+1)
                        root.left = leftchild
                        root.right = rightchild
                        lists[i][i].append(root)
                        for increment in range(1,n+1-i):
                            newroot = TreeNode(m+1+increment)
                            newroot.left = lists[m][m+increment][leftindex]
                            newroot.right = lists[l][i+increment][rightindex]
                            lists[i][i+increment].append(newroot)
        return lists[n][n]

sol = Solution()
list = sol.generateTrees(3)

def printTree(root):
    if root == None:
        print '#',
        return
    print root.val,
    printTree(root.left)
    printTree(root.right)
    
for tree in list:
    printTree(tree)
    print

