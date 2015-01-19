'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
This problem can be solved by breadth-first search:
1. we scan the matrix to find all the 'O's.
2. when an "O" is found, we do the following:
    1. put it into a queue
    2. change its value to "Q" to indicate that it has been put into queue.
    3. then for each element of the queue, we do the following
        1. check if it is close to the boarder if it is then it is not surrounded.
        2. check its neighbours, if a neighbour is "O", change its value to "Q" and put it into the queue.
    4. if the queue is surrounded, change all elements to "X"
3. change all "Q" cells back to "O". These cells are not surrounded.
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