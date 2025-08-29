# 35. Search Insert Position
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

from typing import List, Optional

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1

        return l


class mySolution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # classic binary search bisect left

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2 # (l + (r-l))//2 for overflow avoidance
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:  # nums[mid] > target
                r = mid - 1

        return l


class testcase1:
    nums = [1, 3, 5, 6]
    target = 5
    output = 2

class testcase2:
    nums = [1, 3, 5, 6]
    target = 2
    output = 1

class testcase3:
    nums = [1, 3, 5, 6]
    target = 7
    output = 4

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.searchInsert(testcase1.nums, testcase1.target)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.searchInsert(testcase2.nums, testcase2.target)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.searchInsert(testcase3.nums, testcase3.target)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")