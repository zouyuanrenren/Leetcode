'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
For each row, each column, and each appropriate 3*3 square, use a hashset to maintian the used numbers.
If a number is used twice, return Fasle.
Otherwise, return True.
'''
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for row in range(9):
            used = []
            for col in range(9):
                if board[row][col] in used:
                    return False
                if board[row][col] != '.':
                    used.append(board[row][col])
        for col in range(9):
            used = []
            for row in range(9):
                if board[row][col] in used:
                    return False
                if board[row][col] != '.':
                    used.append(board[row][col])
        for i in range(3):
            for j in range(3):
                used = []
                for row  in range(3*i, 3*(i+1)):
                    for col in range(3*j, 3*(j+1)):
                        if board[row][col] in used:
                            return False
                        if board[row][col] != '.':
                            used.append(board[row][col])
        return True