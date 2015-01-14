'''
Created on 2 Jan 2015

@author: Yuan
'''
'''
Similar as N-Queens, except that no solution is needed, but only the number.
'''
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        result = [0]
        current = []
        self.NQueens(result, current, 0, n)
        return result[0]
    
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
                    result[0] += 1
                else:
                    current.append(col)
                    self.NQueens(result, current, row+1, n)
                    current.pop()


sol = Solution()
results = sol.totalNQueens(1)
print results
        