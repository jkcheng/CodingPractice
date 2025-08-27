# 52. N-Queens II
# Hard
# Topics
# premium lock icon
# Companies
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:
#
# Input: n = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 9

from typing import List,Optional


class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()  # Columns where queens are placed
        p = set()  # Positive diagonals (r+c) occupied by queens
        neg = set()  # Negative diagonals (r-c) occupied by queens
        res = 0  # Result counter
        board = [["."] * n for i in range(n)]  # Board representation

        def bt(r):
            nonlocal res
            if r == n:  # Successfully placed queens in all rows
                res += 1
                return

            for c in range(n):
                # Check if current position conflicts with any queen
                if c in col or (r + c) in p or (r - c) in neg:
                    continue

                # Place queen and update constraints
                col.add(c)
                p.add(r + c)
                neg.add(r - c)
                board[r][c] = 'Q'

                # Recurse to next row
                bt(r + 1)

                # Backtrack: remove queen and constraints
                col.remove(c)
                p.remove(r + c)
                neg.remove(r - c)
                board[r][c] = '.'

        bt(0)  # Start backtracking from row 0
        return res


class mySolution:
    def totalNQueens(self, n: int) -> int:
        # DFS, 2D grid search starting at each square to place queens
        # place queen at board[i][j], mark all queen traversable squares as unplaceable
        # dfs to "neighbors" given by the knight L-shape movement
        # use only first row as starting dfs search to avoid duplicate solutions
        # DOES NOT WORK: has problems when trying to unmark spaces placed by later queens, hard to detect when a square
        # that is attacked by current queen isn't also attacked by a previous queen

        def dfs(i, j, queens):
            nonlocal ans
            # check if outside board
            if (i < 0) or (j < 0) or (i >= n) or (j >= n):
                return

            # check if current location is unplacable
            if board[i][j] == '#':
                return

            # check if number of queens reached
            queens += 1
            if queens == n:
                ans += 1
                return

            # mark unplacable spaces and explore neighbors
            board[i] = ['#'] * n  # mark row
            # mark cols
            for row in range(n):
                board[row][j] = '#'

            # mark diagonals
            for diff in range(-n, n):
                if diff == 1:
                    pass
                if (i + diff >= 0) and (j + diff >= 0) and (i + diff < n) and (j + diff < n):
                    board[i + diff][j + diff] = '#'
                if (i + diff >= 0) and (j - diff >= 0) and (i + diff < n) and (j - diff < n):
                    board[i + diff][j - diff] = '#'

            # check neighbors
            neighbors = [
                (1, 2),
                (2, 1),
                (2, -1),
                (1, -2),
                (-1, -2),
                (-2, -1),
                (-2, 1),
                (-1, 2)
            ]
            for di, dj in neighbors:
                dfs(i + di, j + dj, queens)

            # unmark spaces
            board[i] = ['0'] * n  # mark row
            # mark cols
            for row in range(n):
                board[row][j] = '0'

            # mark diagonals
            for diff in range(-n, n):
                if (i + diff >= 0) and (j + diff >= 0) and (i + diff < n) and (j + diff < n):
                    board[i + diff][j + diff] = '0'
                if (i + diff >= 0) and (j - diff >= 0) and (i + diff < n) and (j - diff < n):
                    board[i + diff][j - diff] = '0'

            return

        # create board
        board = [[0] * n for _ in range(n)]
        ans = 0
        # start search in first row only
        for j in range(n):
            dfs(0, j, 0)

        return ans


class testcase1:
    n = 4
    output = 2

class testcase2:
    n = 1
    output = 1

# ai generated
class testcase3:
    n = 8
    output = 92

# violates constraints lol
class testcase4:
    n = 10
    output = 90

class testcase5:
    n = 12
    output = 724


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.totalNQueens(testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.totalNQueens(testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.totalNQueens(testcase3.n)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )

    # test example 4
    result4 = soln.totalNQueens(testcase4.n)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}" )

    # test example 5
    result5 = soln.totalNQueens(testcase5.n)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {testcase5.output == result5}" )
