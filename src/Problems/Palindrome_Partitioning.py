'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
A typical backtracking problem.
The general idea is:
1. Maintain a list "current" for the partitioned palindromes, initially empty.
1. Given a starting position for the next Palindrome (initially 0), find all possible ending positions.
2. For each of the ending position, add the candidate parlindrome into "current",
    and then recursively find the next palindrome from the next position of the ending position.
    if the next position is beyond the input string, then a result is found.
    remove the current candidate parlindrome from "current".
'''
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        results = []
        current = []
        self.partitionfromStart(s,0,results,current)
        return results
    
    def partitionfromStart(self,s,Start,results,current):
        for end in range(Start+1, len(s)+1):
            pali = True
            for i in range((end-Start)/2):
                if s[Start+i] != s[end-1-i]:
                    pali = False
                    break
            if pali:
                current.append(end)
                if end == len(s):
                    result = [s[0:current[0]]]
                    for i in range(1, len(current)):
                        result.append(s[current[i-1]:current[i]])
                    results.append(result)
                else:
                    self.partitionfromStart(s, end, results, current)
                current.pop()

sol = Solution()
print sol.partition("aasfdadfsaa")    
                    
