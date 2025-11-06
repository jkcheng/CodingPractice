# 724. Find Pivot Index
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.
#
#
#
# Example 1:
#
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
# Example 2:
#
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Example 3:
#
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
#
#
# Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/

from typing import List, Optional

class Solution:
    def pivotIndex(self, nums):
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1


class mySolution:
    def pivotIndex(self, nums: List[int]) -> int:
        # O(n), calculate prefix and suffix sums, then add/delete nums[i] for each i in range(len(nums))
        prefix = 0
        suffix = sum(nums)

        for i, n in enumerate(nums):
            # update suffix
            suffix -= n

            # check if i is pivot
            if prefix == suffix:
                return i

            # update prefix before continuing
            prefix += n

        return -1


class testcase1:
    nums = [1,7,3,6,5,6]
    output = 3

class testcase2:
    nums = [1,2,3]
    output = -1

class testcase3:
    nums = [2,1,-1]
    output = 0


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.pivotIndex(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.pivotIndex(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.pivotIndex(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")