from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        rowtracker = defaultdict(set)
        coltracker = defaultdict(set)
        squaretracker = defaultdict(set)        

        for r in range(row):
            for c in range(col):
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] in rowtracker[r] or \
                    board[r][c] in coltracker[c] or \
                    board[r][c] in squaretracker[r // 3, c //3]:
                        return False
                    else: 
                        rowtracker[r].add(board[r][c])
                        coltracker[c].add(board[r][c])
                        squaretracker[r // 3, c // 3].add(board[r][c])
        return True
