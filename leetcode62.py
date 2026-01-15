# 62. Unique Paths
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.
#
#
#
# Example 1:
#
#
# Input: m = 3, n = 7
# Output: 28
# Example 2:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
#
# Constraints:
#
# 1 <= m, n <= 100

from typing import List, Optional

# 2D DP bottom up: create dp matrix m x n where dp[i][j] represents the # of paths that can reach that cell
# more concise code with better base case handling
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base case: left and top edge cells only have one path to reach
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                # num_paths to reach cell = num_paths from cell above + num_paths from cell to the left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # above + left

        return dp[-1][-1]


class mySolution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2D DP, bottom up, create dp grid of dimensions m*n where dp[m][n] = # ways at that cell can be reached
        # dp[m][n] = dp[m][n-1] + dp[m-1][n]
        # result is at dp[-1][-1]

        dp = [[0] * n] * m

        for i in range(m):
            for j in range(n):
                # starting cell
                if i == 0 and j == 0:
                    dp[i][j] = 1
                # first col
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                # first row
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


class testcase1:
    m = 3
    n = 7
    output = 28

class testcase2:
    m = 3
    n = 2
    output = 3


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.uniquePaths(testcase1.m, testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.uniquePaths(testcase2.m, testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")