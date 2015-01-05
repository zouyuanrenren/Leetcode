'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
This problem can be solved by using backtracking.
The algorithm always remember how many remaining ( and ) need to be generated.
1. start from ( = n and ) = n:
2. if ( = 0:
    a. if ) = 0, then we found a solution
    b. we can generate with ( and )-1
3. otherwise
    a. we can always try (-1 and )
    b. if ) > (, we can also try ( and )-1
'''
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        List = []
        self.addToList(List,"",n,n)
        return List
    def addToList(self,List,string,left,right):
        if left == 0:
            if right == 0:
                List.append(string)
            else:
                self.addToList(List, string+")", left, right-1)
        else:
            self.addToList(List, string+"(", left-1, right)
            if right > left: 
                self.addToList(List, string+")", left, right-1)