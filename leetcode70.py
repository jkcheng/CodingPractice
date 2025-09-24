# 70. Climbing Stairs
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#
# 1 <= n <= 45

from typing import List, Optional


# dp "bottom up" approach: add up previous results
class Solution:
    def climbStairs(self, n: int) -> int:
        # initialize dp array
        # dp array represents the num_ways to reach each step at dp[i]
        dp = [0] * (n + 1)

        # base cases: dp[0] = 1 way to reach "zeroth" step, dp[1] = 1 way to reach 1st step
        dp[0] = 1
        dp[1] = 1

        # dp[i] = dp[i-1] + dp[i-2] : num_ways to reach ith step is the num_ways to reach i-1 step AND num_ways to reach i-2 step
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


class mySolution:
    def climbStairs(self, n: int) -> int:
        # 1D DP: build array where array[i] = number of ways to reach ith step
        # array[i] = array[i-1]+array[i-2]
        # for any given step, add the number of ways to reach the step before and ways to reach two steps before
        dp = [0]*n

        for i in range(len(dp)):
            # base cases: first and second step
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 2
            else:
                dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]


class testcase1:
    n = 2
    output = 2

class testcase2:
    n = 3
    output = 3

# ai generated
class testcase3:
    n = 1
    output = 1


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.climbStairs(testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}" )

    # test example 2
    result2 = soln.climbStairs(testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}" )

    # test example 3
    result3 = soln.climbStairs(testcase3.n)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}" )