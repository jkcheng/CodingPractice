# 45. Jump Game II
# Medium
# Topics
# Companies
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1].
# The test cases are generated such that you can reach nums[n - 1].
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].

# https://leetcode.com/problems/jump-game-ii/solutions/774616/easy-linear-time-o-n-and-space-o-1-explanation
# https://leetcode.com/problems/jump-game-ii/solutions/4339737/jiraiya-s-barrier-technique-linear-solution-intuitive-explanation

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        return


class mySolution:
    def jump(self, nums: List[int]) -> int:
        # O(1000*n) ~ O(n), build dp array in reverse order with dp[i] showing
        # the min number of steps to reach the end from nums[i]
        dp = [0]*len(nums)
        for i in reversed(range(len(nums))):
            if i == len(nums)-1:
                continue
            # special case if nums[i] == 0, set dp[i] to infinity because end cannot be reached
            if nums[i] == 0:
                dp[i] = float('inf')
            else:
                j = nums[i]
                dp[i] = 1+min(dp[i+1:i+j+1])

        return dp[0]


class testcase1:
    nums = [2,3,1,1,4]

class testcase2:
    nums = [2,3,0,1,4]

class testcase3:
    nums = [3,1,2,1,4]