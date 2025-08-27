# 189. Rotate Array
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
#
#
# Follow up:
#
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# https://leetcode.com/problems/rotate-array/solutions/269948/4-solutions-in-python-from-easy-to-hard

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        return


class mySolution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n), O(1) space, rotate array once to final configuration by copy each nums[i] to nums[i+k]
        # copy existing value to temporary variable, continue copying values until all indexes of nums visited
        # return unchanged nums if k is multiple of len(nums)
        if k == len(nums):
            return

        visited = sum(range(len(nums)+1))
        start = 0
        while visited > 0:
            # need to add cycle detection
            i = start
            next_val = None
            while True:
                next_idx = (i+k) % len(nums)
                old_val = next_val if next_val != None else nums[i]
                next_val = nums[next_idx]
                nums[next_idx] = old_val
                visited -= (i+1)
                i = next_idx

                # break out of loop if cycle detected
                if i == start:
                    break

            start = i+1

        return


class testcase1:
    nums = [1,2,3,4,5,6,7]
    k = 3

class testcase2:
    nums = [-1,-100,3,99]
    k = 2

# class testcase3:
#     nums = [2,2,1,3,2,2,5]