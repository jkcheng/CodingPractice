# 120. Triangle
# Medium
# Topics
# premium lock icon
# Companies
# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
#
#
#
# Example 1:
#
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:
#
# Input: triangle = [[-10]]
# Output: -10
#
#
# Constraints:
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
#
#
# Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?

from typing import List, Optional


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        return


class mySolution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 2d dp: construct triangle dp arry with same dimensions as original
        # dp[i][j] = minimum path sum to reach this position
        # dp[i][j] = triangle[i][j]+min(triangle[i-1][j-1],triangle[i-1][j])

        dp = [[0] * len(row) for row in triangle]

        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                # edge cases
                if i == 0 and j == 0:  # first value
                    dp[i][j] = triangle[i][j]
                elif j == 0:  # left edge
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j == len(triangle[i]) - 1:  # right edge, j == i also works
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])

        return min(dp[-1])  # return minimum of last row


class testcase1:
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    output = 11

class testcase2:
    triangle = [[-10]]
    output = -10

# ai generated, corrected
class testcase3:
    # triangle = [[-10],[-10]] # invalid ai generated triangle
    triangle = [[-10], [-10, -90]]
    output = -100


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.minimumTotal(testcase1.triangle)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.minimumTotal(testcase2.triangle)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.minimumTotal(testcase3.triangle)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")