# 64. Minimum Path Sum
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
#
#
# Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200

from typing import List, Optional


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        return


class mySolution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # O(2^(m+n)), recursively dfs right and down and return shortest sum, can improve with memo
        # 2d dp, create m x n dp grid containing min path sums and fill from bottom right
        # dp[i][j] = min path sum from this square
        # dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        dp = [[0]*len(row) for row in grid]

        m = len(grid)
        n = len(grid[0])
        # iterate backwards and fill dp from bottom right
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # bottom right corner
                if i == m-1 and j == n-1:
                    dp[i][j] = grid[i][j]
                elif i == m-1: # bottom row
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                elif j == n-1: # right col
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]


class testcase1:
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    output = 7

class testcase2:
    grid = [[1,2,3],[4,5,6]]
    output = 12


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.minPathSum(testcase1.grid)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.minPathSum(testcase2.grid)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")
