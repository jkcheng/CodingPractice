# 283. Move Zeroes
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
#
#
# Follow up: Could you minimize the total number of operations done?

from typing import List, Optional


# O(n) time, O(1) space: use left, right pointers
# left pointer to refer to leftmost zero, right pointer iterates through array and swaps position with left pointer when non-zero value
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointers: maintaing rear pointer at trailing edge of zeroes
        # swap values with forward pointer when encountering non-zero
        # move rear pointer one position forward to maintain trailing zero

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                # swap values
                nums[l], nums[r] = nums[r], nums[l]
                # increment l pointer
                l += 1

        return nums


class mySolution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer, maintain slow pointing at leading edge of zeros
        slow, fast = 0, 0

        while fast < len(nums):
            # swap values at slow fast pointer if nonzero
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

            fast += 1

        return nums


class testcase1:
    nums = [0,1,0,3,12]
    output = [1,3,12,0,0]

class testcase2:
    nums = [0]
    output = [0]

class testcase3:
    nums = [-1,12,0,0,0,0,0,0]
    output = [-1,12,0,0,0,0,0,0]

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.moveZeroes(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.moveZeroes(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.moveZeroes(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")