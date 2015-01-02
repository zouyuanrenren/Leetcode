'''
Created on 2 Jan 2015

@author: Yuan
'''
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []
        current = []
        self.NQueens(result, current, 0, n)
        return result
    
    def NQueens(self, result, current, row, n):
        for col in range(n):
            clash = False
            for i in range(len(current)):
                if col == current[i] or abs(row-i) == abs(col-current[i]):
                    clash = True
                    break
            if not clash:
                if row == n-1:
                    # found a solution
                    current.append(col)
                    newresult = []
                    for i in range(n):
                        str = ""
                        for j in range(current[i]):
                            str+="."
                        str+="Q"
                        for j in range(current[i]+1, n):
                            str+="."
                        newresult.append(str)
                    result.append(newresult)
                else:
                    current.append(col)
                    self.NQueens(result, current, row+1, n)
                current.pop()


sol = Solution()
results = sol.solveNQueens(1)
for result in results:
    for row in result:
        print row
    print
