'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
A typical backtracking problem.
Maintain a dictionary of number and its associated letters.
Then go through the string, for each digit, try all possible letters
'''
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        Dict = {'2':"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        Results = []
        if len(digits) == 0:
            return [""]
        self.addString(Dict, Results, digits, "", 0)
        return Results
    
    def addString(self, Dict, Results, digits, current, index):
        for c in Dict[digits[index]]:
            current +=c
            if index == len(digits)-1:
                Results.append(current)
            else:
                self.addString(Dict, Results, digits, current, index+1)
            current = current[:-1]