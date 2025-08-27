# 238. Product of Array Except Self
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        return


class mySolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # O(n) time, O(n) space, build two arrays left and right, where
        # # left[i] is the product of all values left of nums[i]
        # # right[i] is product of all values right of nums[i]
        # # solution is left[i]*right[i]
        # left, right = [1]*len(nums), [1]*len(nums)
        # prod = 1
        # for i,n in enumerate(nums):
        #     left[i] = prod
        #     prod *= n
        #
        # prod = 1
        # for i in reversed(range(len(nums))):
        #     right[i] = prod
        #     prod *= nums[i]
        #
        # return [left[i]*right[i] for i in range(len(nums))]

        # O(n) time, O(1) space, multiply products in-place in final output array
        ans = [1]*len(nums)

        # build left products
        prod = 1
        for i,n in enumerate(nums):
            ans[i] = prod
            prod *= n

        # build right product and multiply with ans
        prod = 1
        for i in reversed(range(len(nums))):
            ans[i] = ans[i]*prod
            prod *= nums[i]

        return ans

class testcase1:
    nums = [1,2,3,4]

class testcase2:
    nums = [-1,1,0,-3,3]

class testcase3:
    nums = [3,1,2,1,4]
