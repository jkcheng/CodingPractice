# 167. Two Sum II - Input Array Is Sorted
# Solved
# Medium
# Topics
# Companies
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as
# an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.
#
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
#
#
# Constraints:
#
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solutions/580496/python-short-two-pointer-solution-with-explanation

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two-pointer, O(n) with O(1) space, check sum of numbers[l] and numbers[r]
        # increase l if sum too small, decrease r if sum too large
        l, r = 0, len(numbers)-1
        while l < r:
            tot = numbers[l] + numbers[r]
            if tot == target:
                return [l+1, r+1]
            elif tot < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]


class mySolution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # linear scan array, binary search rest of array for complement
        def binsearch(l, r, nums, complement):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == complement:
                    return mid
                elif nums[mid] < complement:
                    l = mid+1
                else:
                    r = mid-1

            return -1

        for i,n in enumerate(numbers):
            complement = target - n
            # binary search rest of array
            comp_idx = binsearch(i+1, len(numbers)-1, numbers, complement)

            if comp_idx != -1:
                return [i+1, comp_idx+1]

        return None


class testcase1:
    numbers = [2, 7, 11, 15]
    target = 9

class testcase2:
    numbers = [2, 3, 4]
    target = 6

class testcase3:
    numbers = [-1, 0]
    target = -1