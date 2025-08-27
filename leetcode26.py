# 26. Remove Duplicates from Sorted Array
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:
#
# The judge will test your solution with the following code:
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return


class mySolution:
    # O(n): two pointers, linear scan array and add elements to a set.
    # If not in set, swap position with leading pointer and increment rear pointer, maintains rear pointer at first duplicate element.
    def removeDuplicates(self, nums: List[int]) -> int:
        # pt = 0
        # seen = set()
        # for i, n in enumerate(nums):
        #     if n not in seen:
        #         seen.add(n)
        #         nums[i], nums[pt] = nums[pt], nums[i]
        #         pt += 1

        # space optimization: insteead of a hash table lookup, check if current value n is greater than nums[pt]
        # we can do this because input is guaranteed to be non-decreasing
        pt = 0
        for i, n in enumerate(nums):
            if pt == 0 or n > nums[pt-1]:
                nums[i], nums[pt] = nums[pt], nums[i]
                pt += 1
        return pt


class testcase1:
    nums = [1,1,2]

class testcase2:
    nums = [0,0,1,1,1,2,2,3,3,4]

class testcase3:
    nums = [0,0,0,0,0,0]

class testcase4:
    nums = [5]
