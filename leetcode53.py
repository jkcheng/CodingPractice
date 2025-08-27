# 53. Maximum Subarray
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List, Optional


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        return


class mySolution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm: at each step compare two things
        # adding current value to running sum vs starting a new subarray
        # max sum using current value (the output of previous comparison) vs global max so far

        global_max = float('-inf')
        curr_max = float('-inf')
        for n in nums:
            curr_max = max(curr_max + n, n)
            global_max = max(global_max, curr_max)

        return global_max


class testcase1:
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output = 6

class testcase2:
    nums = [1]
    output = 1

class testcase3:
    nums = [5,4,-1,7,8]
    output = 23

# ai generated
class testcase4:
    nums = [-2,-3,-1]
    output = -1

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.maxSubArray(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.maxSubArray(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.maxSubArray(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.maxSubArray(testcase4.nums)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")