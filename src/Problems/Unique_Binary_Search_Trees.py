'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
This problem can be solved by dynamic programming.
Note that the left child and right child of a binary search tree are also binary search trees.
Let us use List and use List[i] to represent the number of unique binary search tree of size i.
Then for tree size n,
    for each i in range(n)
    the number of unique search tree with i+1 as the root is List[i] * List[n-i-1].
'''
class Solution:
    # @return an integer
    def numTrees(self, n):
        List = [1,1]
        for num in range(2,n+1):
            result = 0
            for i in range(num):
                result += List[i]*List[num-i-1]
            List.append(result)
        return List[n]
        