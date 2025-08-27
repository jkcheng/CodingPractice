# 80. Remove Duplicates from Sorted Array II
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums sorted in non-decreasing order,
# remove some duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
#
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
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
#
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/solutions/27976/3-6-easy-lines-c-java-python-ruby

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return


class mySolution:
    # O(n): two pointer, linear scan array and maintain slow pointer at first index outside of valid values
    # If valid value encountered then copy value at current index to value slow position, increment slow
    # Because input is non-decreasing, can use nums[i] > nums[slow-2] as valid criteria
    # Only start checking at values i > 1, because first two values in array are guaranteed to be valid
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for i,n in enumerate(nums):
            # if valid, then copy value to nums[slow-2]
            if (i < 2) or ((i > 1) and (n > nums[slow-2])):
                nums[slow] = n
                slow += 1


        return slow


class testcase1:
    nums = [1,1,1,2,2,3]

class testcase2:
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

# class testcase3:
#     nums = [7,7,7,7,7,7,7]
#
# class testcase4:
#     nums = [14,4,6,