# 790. Domino and Tromino Tiling
# Medium
# Topics
# premium lock icon
# Companies
# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
#
#
# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
#
# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
#
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
# Explanation: The five different ways are shown above.
# Example 2:
#
# Input: n = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 1000

from typing import List, Optional


# https://leetcode.com/problems/domino-and-tromino-tiling/solutions/6172161/intuitive-approach-using-3-dp-arrays-by-ifmhm
class Solution:
    def numTilings(self, n: int) -> int:
        # dynamic programming
        # note: F = Full, T = TopMissing, B = BottomMissing

        F = {0: 1, 1: 1}
        T = {1: 0}
        B = {1: 0}

        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2] + T[i - 1] + B[i - 1]
            T[i] = F[i - 2] + B[i - 1]
            B[i] = F[i - 2] + T[i - 1]

        return F[n] % (10 ** 9 + 7)

class mySolution:
    def numTilings(self, n: int) -> int:
        # n == 0, output = 0
        # n == 1, output = 1
        # n == 2, output = 2
        # n == 3, output = 5
        # n == 4, output = ??
        # O(n), 1D DP, dp array of length n with dp[n] is the num ways to fill out 2*n board
        # dp[n] = (every possible final shape filling up the last column) + dp[n-x], where x depends on the final shape
        # see https://leetcode.com/problems/domino-and-tromino-tiling/solutions/116664/schematic-explanation-of-two-equivalent-2nr0u for detailed explanation

        mod = 1e9 + 7
        p1 = 1
        p2 = 0
        p3 = -1

        for i in range(1, n + 1):
            cur = (2 * p1 + p3) % mod
            p3 = p2
            p2 = p1
            p1 = cur

        return int(p1)


class testcase1:
    n = 3
    output = 5

class testcase2:
    n = 1
    output = 1


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.numTilings(testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.numTilings(testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")