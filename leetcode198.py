# 198. House Robber
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

from typing import List, Optional

# 1D DP solution: bottom up, space optimized
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case
        prev1 = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):
            cur = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = cur

        return prev1


class mySolution:
    def rob(self, nums: List[int]) -> int:
        # 1d dp: create array of max money where array[i] = max(array[i-1], nums[i]+array[i-2])
        # array[i] represents solution to the problem at house i
        # max amount robbed at house i = max(rob curr house + two houses prev, skip curr + rob prev house)
        dp = [0] * len(nums)  # space optimization: just store prev & two_prev as variables instead of dp array
        for i in range(len(nums)):
            # base cases, first and second house
            if i == 0:
                dp[i] = nums[i]  # rob current, only one available
            elif i == 1:
                dp[i] = max(nums[i - 1], nums[i])  # rob prev or current
            else:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])  # rob curr + two houses prev or skip curr + prev

        return dp[-1]


class testcase1:
    nums = [1, 2, 3, 1]
    output = 4

class testcase2:
    nums = [2, 7, 9, 3, 1]
    output = 12

# ai generated
class testcase3:
    nums = [1, 2, 3, 1, 1]
    output = 5 # original ai answer = 4 wrong!


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.rob(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.rob(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.rob(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")