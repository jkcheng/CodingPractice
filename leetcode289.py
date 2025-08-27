# 289. Game of Life
# Solved
# Medium
# Topics
# Companies
# According to Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# The board is made up of an m x n grid of cells, where each cell has an initial state:
# live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
# using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell
# in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.
#
# Given the current state of the board, update the board to reflect its next state.
#
# Note that you do not need to return anything.
#
#
#
# Example 1:
#
#
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# [[0,1,0],
#  [0,0,1],
#  [1,1,1],
#  [0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:
#
#
# Input: board = [[1,1],[1,0]]
# [[1,1],
#  [1,0]]
# Output: [[1,1],[1,1]]
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
#
#
# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated simultaneously:
# You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array.
# In principle, the board is infinite, which would cause problems when the active area encroaches upon the border
# of the array (i.e., live cells reach the border). How would you address these problems?

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        return

# O(1) space, O(n): add 2 to each cell that would be alive in next generation
# use cell%2==1 to check for current state (adding 2 does not change cell%2 value for current state)
# perform second pass to update cells to alive or dead in next generation based on +2 value
class mySolution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # mark cells to be alive by adding 2, use %2 to check current state
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i in range(m):
            for j in range(n):
                alivecount = 0
                for k,l in neighbors:
                    newi = i+k
                    newj = j+l
                    # check new coords are in boundary
                    if newi >= 0 and newi < m and newj >= 0 and newj < n:
                        neib = board[newi][newj]
                        alivecount += (neib % 2) # add either 1 or 0 to alive count

                # check if cell should be alive next gen and flag
                if alivecount == 3:
                    board[i][j] += 2
                elif alivecount == 2 and board[i][j] == 1:
                    board[i][j] += 2

        # update board to next state
        for i in range(m):
            for j in range(n):
                if board[i][j] >= 2:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

        return board

class testcase1:
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

class testcase2:
    board = [[1, 1], [1, 0]]