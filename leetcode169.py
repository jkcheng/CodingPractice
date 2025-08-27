# 169. Majority Element
# Solved
# Easy
# Topics
# Companies
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
#
#
#
# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
# follow up solution uses: https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return


class mySolution:
    def majorityElement(self, nums: List[int]) -> int:
        # # hashmap counting
        # counts = {}
        # for n in nums:
        #     counts[n] = counts.get(n,0)+1
        #     if counts[n] > len(nums)/2:
        #         return n
        #
        # return

        # Boyer-Moore majority vote algorithm
        count = 0
        candidate = None
        for n in nums:
            if candidate is not None and n == candidate:
                count += 1
            elif count == 0:
                candidate = n
                count = 1
            else:
                count -= 1

        return candidate

class testcase1:
    nums = [3,2,3]

class testcase2:
    nums = [2,2,1,1,1,2,2]

class testcase3:
    nums = [2,2,1,3,2,2,5]