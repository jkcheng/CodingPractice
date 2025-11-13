# 2352. Equal Row and Column Pairs
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
#
#
#
# Example 1:
#
#
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:
#
#
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105

from typing import List, Optional


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        rows = {}

        for r in range(n):
            row = tuple(grid[r])
            rows[row] = 1 + rows.get(row, 0)

        for c in range(n):
            col = tuple(grid[i][c] for i in range(n))
            count += rows.get(col, 0)

        return count


class mySolution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # O(n^3), copy and transpose matrix, then compare each row with each col
        n = len(grid)

        # # create transposed matrix
        # transposed = []
        # for i in range(n):
        #     col = [0]*n
        #     for j in range(n):
        #         col[j] = grid[j][i]

        #     transposed.append(col)

        # O(n^2), optimization: create hashed tuples of rows & cols
        transposed = []
        for i in range(n):
            col = [0] * n
            for j in range(n):
                col[j] = grid[j][i]

            transposed.append(hash(tuple(col)))

        grid = [hash(tuple(row)) for row in grid]

        # compare rows and cols
        count = 0
        for row in grid:
            for col in transposed:
                if row == col:
                    count += 1

        return count

class mySolution2:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # O(n^2), create dictionary with rows as tuples as key and count as values
        # iterate through cols and compare to dict for existence

        # create dict of rows as tuples
        rows = {}
        for row in grid:
            t = tuple(row)
            rows[t] = rows.get(t, 0) + 1

        # create tuple col and compare to dict
        n = len(grid)
        count = 0
        for i in range(n):
            t = tuple(grid[j][i] for j in range(n))
            count += rows.get(t, 0)

        return count

class testcase1:
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    output = 1

class testcase2:
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    output = 3

# ai generated
class testcase3:
    grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    output = 0


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.equalPairs(testcase1.grid)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.equalPairs(testcase2.grid)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.equalPairs(testcase3.grid)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")