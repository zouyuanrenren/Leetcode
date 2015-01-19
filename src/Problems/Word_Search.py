'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
A depth-first search problem and can be solved with backtracking.
For each character in the matrix find out if the character can be used as the 0th character in the word.
A character can be used as the ith character in the word IFF
    1. it is the same as the ith character in the word.
    2. one of its neighbours has not been used yet and can be used as the i+1th character in the word.
'''
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if len(board) == 0 or len(board[0]) == 0:
            return len(word) == 0
        h = len(board)
        w = len(board[0])
        for i in range(h):
            for j in range(w):
                if self.findNext(board, i, j, [], 0, word):
                    return True
        return False
    
    def findNext(self, board, i, j, stack, next, word):
        if next == len(word) or board[i][j] != word[next]:
            return False
        if next == len(word) -1:
            return True
        stack.append([i,j])
        h = len(board)
        w = len(board[0])
        if i > 0  and [i-1, j] not in stack and self.findNext(board, i-1,j,stack,next+1, word):
            return True
        if i < h-1 and [i+1, j] not in stack and self.findNext(board, i+1, j, stack, next+1, word):
            return True
        if j >0 and [i, j-1] not in stack and self.findNext(board, i, j-1, stack, next+1, word):
            return True
        if j < w -1 and [i,j+1 ] not in stack and self.findNext(board, i, j+1, stack, next+1, word):
            return True
        stack.pop()
        return False
    
board = [
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"]
]
word = "ABCC"
sol = Solution()
print sol.exist(board, word)