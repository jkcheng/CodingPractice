# 55. Jump Game
# Solved
# Medium
# Topics
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return


class mySolution:
    def canJump(self, nums: List[int]) -> bool:
        # nums = [3,2,1,0,4]
        # O(n): linear scan array, update available remaining steps if nums[i] > available steps.
        # Decrement available steps with each iteration
        availablesteps = 0
        steps_taken = 0
        for i,n in enumerate(nums):
            steps_taken += 1
            if n > availablesteps:
                availablesteps = n

            if availablesteps == 0:
                break
            availablesteps -= 1

        return True if steps_taken == len(nums) else False


class testcase1:
    nums = [2,3,1,1,4]

class testcase2:
    nums = [3,2,1,0,4]

class testcase3:
    nums = [3,5,2,1,4]