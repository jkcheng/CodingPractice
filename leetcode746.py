# 746. Min Cost Climbing Stairs
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
#
# Example 1:
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
#
#
# Constraints:
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

from typing import List, Optional

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp array, stores MIN cost of leaving this step
        cost.append(0)
        n = len(cost)
        dp = [0] * (n)

        # base case: step 0 & 1
        dp[0] = cost[0]
        dp[1] = cost[1]

        # calculate cost of leaving each step as min of cost to reach step + cost of step
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])


class mySolution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(n), dp, create array of length n+1, dp[n] = min(dp[n-1],dp[n-2]) + cost[n]
        # dp[n] represents min total cost to reach step n
        # d[0], dp[1] default to cost[0], cost[1]

        # add 0 to end of cost for the last step
        cost.append(0)
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for n in range(2, len(dp)):
            dp[n] = min(dp[n - 1], dp[n - 2]) + cost[n]

        return dp[-1]

# naive iterative attempt, will result in incorrect answer
class mySolution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalcost = 0
        i = 0
        while i < len(cost) - 1:
            if cost[i] < cost[i + 1]:
                totalcost += cost[i]
                i += 1
            else:
                totalcost += cost[i + 1]
                i += 2

        return totalcost


class testcase1:
    cost = [10, 15, 20]
    output = 15

class testcase2:
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    output = 6


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.minCostClimbingStairs(testcase1.cost)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.minCostClimbingStairs(testcase2.cost)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")