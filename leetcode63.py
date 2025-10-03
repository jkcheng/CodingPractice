# 63. Unique Paths II
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.
#
#
#
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
# Constraints:
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.

from typing import List, Optional


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        return


class mySolution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # O(2^n) (?), recursively explore each grid space and add up number of paths that can pass through each space
        # grid[i][j] is number_paths(grid[i-1][j]) + number_paths(grid[i][j-1])
        # can reduce redundant work by memoizing
        # O(n), 2d dp, create m x n dp array with number of paths going through each space
        # dp[i][j] = dp[i-1][j] + dp[i][j-1] if no obstacle
        # can reuse grid for space optimization

        grid = obstacleGrid
        dp = [[0] * len(row) for row in grid]  # create copy of grid
        m = len(dp)
        n = len(dp[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:  # top left
                    if grid[i][j] == 1 or grid[-1][-1] == 1:  # starting/ending space is blocked, no path possible
                        return 0
                    else:
                        dp[i][j] = 1
                elif i == 0 and grid[i][j - 1] != 1:  # top edge
                    dp[i][j] = dp[i][j - 1]
                elif j == 0 and grid[i - 1][j] != 1:  # left edge
                    dp[i][j] = dp[i - 1][j]
                else:
                    from_left = dp[i][j - 1] if grid[i][j - 1] != 1 else 0
                    from_top = dp[i - 1][j] if grid[i - 1][j] != 1 else 0
                    dp[i][j] = from_left + from_top

        return dp[-1][-1]


class testcase1:
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    output = 2

class testcase2:
    obstacleGrid = [[0,1],[0,0]]
    output = 1

class testcase3:
    obstacleGrid = [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]]
    output = 8

class testcase4:
    obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]]
    output = 6

class testcase5:
    obstacleGrid = [[0,0],[0,1]]
    output = 0


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.uniquePathsWithObstacles(testcase1.obstacleGrid)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.uniquePathsWithObstacles(testcase2.obstacleGrid)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.uniquePathsWithObstacles(testcase3.obstacleGrid)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.uniquePathsWithObstacles(testcase4.obstacleGrid)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.uniquePathsWithObstacles(testcase5.obstacleGrid)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")