# 130. Surrounded Regions
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#
# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
#
#
#
# Example 1:
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Explanation:
#
#
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
#
# Example 2:
#
# Input: board = [["X"]]
#
# Output: [["X"]]
#
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

from typing import List, Optional


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(m, n):
            # check out of bounds
            if (m < 0) or (n < 0) or (m >= rows) or (n >= cols):
                return

            if (board[m][n] == 'O'):
                board[m][n] = 'T'
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dm, dn in dirs:
                    dfs(m + dm, n + dn)

        # dfs from edges of board and mark all uncapturable 'O' as 'T'
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # mark all 'T' as 'O', and all others as 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'


class mySolution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS two-pass, explore all O starting from edges and mark as not-surrounded
        # scan entire board and mark all not-surrounded O with X

        m = len(board)
        n = len(board[0])
        grid = board

        def mark_not_surrounded(i, j):
            # check if out of bounds
            if (i < 0) or (j < 0) or (i >= m) or (j >= n):
                return

            # explore
            if grid[i][j] == 'O':
                # mark as not surrounded
                grid[i][j] = '#'
                # check neighbors
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for di, dj in directions:
                    mark_not_surrounded(i + di, j + dj)

        # explore left and right edge
        for i in range(0, m):
            for j in (0, n - 1):
                # explore if cell is initially '0'
                if grid[i][j] == 'O':
                    mark_not_surrounded(i, j)

        # explore top and bottom edge
        for i in (0, m - 1):
            for j in range(0, n):
                # explore if cell is initially '0'
                if grid[i][j] == 'O':
                    mark_not_surrounded(i, j)

        # mark all remaining '0' and 'X'
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
                # unmark # as O
                elif grid[i][j] == '#':
                    grid[i][j] = 'O'


class testcase1:
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

class testcase2:
    board = [["X"]]
    output = [["X"]]

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    soln.solve(testcase1.board)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {testcase1.board}, Correct: {testcase1.output == testcase1.board}" )

    # test example 2
    soln.solve(testcase2.board)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {testcase2.board}, Correct: {testcase2.output == testcase2.board}" )