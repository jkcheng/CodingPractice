# 36. Valid Sudoku
# Solved
# Medium
# Topics
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
#
# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(len(board)):
            rowset = set()
            for j in range(len(board[i])):
                if board[i][j] != '.' and board[i][j] in rowset:
                    return False
                else:
                    rowset.add(board[i][j])

        # cols
        for i in range(len(board)):
            colset = set()
            for j in range(len(board[i])):
                if board[j][i] != '.' and board[j][i] in colset:
                    return False
                else:
                    colset.add(board[j][i])

        # 3x3s
        for i in range(len(board)):
            if i % 3 == 0:  # create new sets when i is divisible by 3
                threeset1 = set()
                threeset2 = set()
                threeset3 = set()

            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if 0 <= j <= 2:
                        if board[i][j] in threeset1:
                            return False
                        else:
                            threeset1.add(board[i][j])

                    elif 3 <= j <= 5:
                        if board[i][j] in threeset2:
                            return False
                        else:
                            threeset2.add(board[i][j])

                    elif 6 <= j <= 8:
                        if board[i][j] in threeset3:
                            return False
                        else:
                            threeset3.add(board[i][j])

        return True

# O(m+n): iteratively check each row, col, and 3x3 grid using a set to check if number already exists
class mySolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows & cols
        rowsets = [set() for _ in range(9)]
        colsets = [set() for _ in range(9)]
        gridsets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                n = board[i][j]
                if n != '.':
                    # return false if number already in row or col
                    gridi = i//3
                    gridj = j//3
                    if n in rowsets[i] or n in colsets[j] or n in gridsets[gridi][gridj]:
                        return False
                    else:
                        rowsets[i].add(n)
                        colsets[j].add(n)
                        gridsets[gridi][gridj].add(n)

        return True

class testcase1:
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

class testcase2:
    board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
