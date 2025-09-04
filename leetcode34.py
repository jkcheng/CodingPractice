# 34. Find First and Last Position of Element in Sorted Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

from typing import List, Optional


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # search for left edge
        l, r = 0, len(nums) - 1

        lefti = None
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    if lefti == None:
                        lefti = mid
                    else:
                        lefti = min(lefti, mid)
                r = mid - 1
            else:
                l = mid + 1

        # return early if target not found at all
        if lefti == None:
            return [-1, -1]

        # search for right edge if lefti is found
        righti = None
        l, r = lefti, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                if righti == None:
                    righti = mid
                else:
                    righti = max(righti, mid)
                l = mid + 1
            else:
                r = mid - 1

        return


class mySolution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search twice to find left and right edges

        # left edge
        l, r = 0, len(nums) - 1
        lefti = None
        while l <= r:
            mid = (l + r) // 2  # (l + (r-l))//2 to avoid overflow
            if nums[mid] >= target:
                if nums[mid] == target:
                    lefti = min(lefti, mid) if lefti != None else mid
                r = mid - 1
            else:
                l = mid + 1

        # right edge
        l, r = 0, len(nums) - 1
        righti = None
        while l <= r:
            mid = (l + r) // 2  # (l + (r-l))//2 to avoid overflow
            if nums[mid] <= target:  # search right
                if nums[mid] == target:
                    righti = max(righti, mid) if righti is not None else mid
                l = mid + 1
            else:
                r = mid - 1

        return [lefti, righti] if lefti is not None and righti is not None else [-1, -1]


class testcase1:
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    output = [3, 4]

class testcase2:
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    output = [-1, -1]

class testcase3:
    nums = []
    target = 0
    output = [-1, -1]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.searchRange(testcase1.nums, testcase1.target)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.searchRange(testcase2.nums, testcase2.target)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.searchRange(testcase3.nums, testcase3.target)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")