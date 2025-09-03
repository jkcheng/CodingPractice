# 33. Search in Rotated Sorted Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

from typing import List, Optional


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # key insight: check if mid and target are in same or different halves
            # same half = standard binary search (left if target<mid, right if target>mid)
            # diff half = opposite (right if target<mid, left if target>mid)
            # check for same half
            if (nums[mid] >= nums[0] and target >= nums[0]) or (nums[mid] < nums[0] and target < nums[0]):
                # # more concise if:
                # if (nums[mid] >= nums[0]) == (target >= nums[0]):
                # standard binary search
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # diff half
                # opposite
                if target < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


class mySolution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search, compare target with nums[mid] and nums[mid] with nums[0]
        # compare target to nums[0] to determine whether target and nums[mid] are in same half of array
        # if same half, standard binary search
        # else opposite

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r)//2 # (l + (r-l))//2 to avoid overflow
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                if (target >= nums[0] and nums[mid] >= nums[0]) or (target < nums[0] and nums[mid] < nums[0]): # same halves, search right
                    l = mid + 1
                else: # different halves
                    r = mid - 1
            else: # target < nums[mid]
                if (target >= nums[0] and nums[mid] >= nums[0]) or (target < nums[0] and nums[mid] < nums[0]): # same halves, search left
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


class testcase1:
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    output = 4

class testcase2:
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    output = -1

class testcase3:
    nums = [1]
    target = 0
    output = -1

class testcase4:
    nums = [1, 3, 5]
    target = 5
    output = 2

class testcase5:
    nums = [1, 3, 5]
    target = 1
    output = 0


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.search(testcase1.nums, testcase1.target)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.search(testcase2.nums, testcase2.target)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.search(testcase3.nums, testcase3.target)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.search(testcase4.nums, testcase4.target)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.search(testcase5.nums, testcase5.target)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")
