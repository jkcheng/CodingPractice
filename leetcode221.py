# 221. Maximal Square
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:
#
# Input: matrix = [["0"]]
# Output: 0
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.

# https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach

from typing import List, Optional


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        return


class mySolution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # O(m*n), 2d dp, create dp array representing largest square formed at each cell
        # Count each '1' cell and +1 if all other neighbors are also 1
        # dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + matrix[i][j] if matrix[i][j] == 1

        # dp is (m+1)*(n+1) to facilitate edge cases
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_square = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                # set dp[i][j] to min(neighbors) + 1 if matrix[i][j] == '1'
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 # or + matrix[i-1][j-1]
                    max_square = max(max_square, dp[i][j])

        return max_square**2


class testcase1:
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    output = 4

class testcase2:
    matrix = [["0","1"],["1","0"]]
    output = 1

class testcase3:
    matrix = [["0"]]
    output = 0


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.maximalSquare(testcase1.matrix)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.maximalSquare(testcase2.matrix)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.maximalSquare(testcase3.matrix)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")