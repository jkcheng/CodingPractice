# 209. Minimum Size Subarray Sum
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.
#
#
#
# Example 1:
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
# Constraints:
#
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
#
#
# Follow up: If you have figured out the O(n) solution,
# try coding another solution of which the time complexity is O(n log(n)).

# https://leetcode.com/problems/minimum-size-subarray-sum/solutions/1037095/python-3-two-pointer-while-loop-illustrated

from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        i, j = 0, 0
        c, t = float("inf"), nums[0]
        while j <= len(nums)-1:
            if t < s:
                j += 1
                if j <= len(nums)-1:
                    t += nums[j]
            elif t >= s:
                c = min(j - i + 1, c)
                t -= nums[i]
                i += 1
        return c if c != float("inf") else 0


class mySolution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n), sliding window, grow window until sum > target
        # shrink window until sum < target, grow window again
        l, r = 0, 0

        tot = nums[r]
        minwindow = len(nums)
        total_achieved = False
        while r < len(nums) - 1 or tot >= target:

            # try growing right edge
            while r < len(nums) - 1 and tot < target:
                r += 1
                tot += nums[r]

            # try shrinking left edge
            while l <= r and tot >= target:
                minwindow = min(minwindow, r - l + 1)
                if tot >= target:
                    total_achieved = True
                tot -= nums[l]
                l += 1

        return minwindow if total_achieved else 0

class mySolution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n), sliding window, grow window if total < target
        # shrink window until total >= target
        # repeat until end of array found, return windowsize if not initial value
        l, r = 0, 0
        total = 0
        windowsize = float('inf')
        total = nums[r]
        while r < len(nums):
            # move r and grow window if < target
            if total < target:
                # attempt to grow window and add to total if still valid
                r += 1
                if r < len(nums):
                    total += nums[r]
            # move l and shrink window if >= target
            else: # total >= target
                windowsize = min(windowsize, r-l+1)
                total -= nums[l]
                l += 1

        return windowsize if windowsize < float('inf') else 0


class testcase1:
    target = 7
    nums = [2, 3, 1, 2, 4, 3]

class testcase2:
    target = 4
    nums = [1, 4, 4]

class testcase3:
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]

class testcase4:
    target = 5
    nums = [1,1,2,0]