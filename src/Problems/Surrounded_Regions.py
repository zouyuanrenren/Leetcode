'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] == "O":
                    queue = []
                    self.addToQueue(queue,board,i,j)
                    index = 0
                    surrounded = True
                    while index < len(queue):
                        row = queue[index][0]
                        col = queue[index][1]
                        if row -1 >=0:
                            if board[row-1][col] == "O":
                                self.addToQueue(queue, board, row-1, col)
                        else:
                            surrounded = False
                        if row +1 < h:
                            if board[row+1][col] == "O":
                                self.addToQueue(queue, board, row+1, col)
                        else:
                            surrounded = False
                        if col -1 >= 0:
                            if board[row][col-1] == "O":
                                self.addToQueue(queue, board, row, col-1)
                        else:
                            surrounded = False
                        if col+1 < w:
                            if board[row][col+1] == "O":
                                self.addToQueue(queue, board, row, col+1)
                        else:
                            surrounded = False
                        index += 1
                    if surrounded:
                        for cell in queue:
                            board[cell[0]][cell[1]] = "X"
        for i in range(h):
            for j in range(w):
                if board[i][j] == "Q":
                    board[i][j] = "O"

    def addToQueue(self,queue,board,i,j):        
        board[i][j] = "Q"
        queue.append([i,j])
 

board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]

sol = Solution()
sol.solve(board)
print board   