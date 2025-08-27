# 918. Maximum Sum Circular Subarray
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
#
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
#
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
#
#
#
# Example 1:
#
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:
#
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:
#
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104

from typing import List, Optional


class Solution:
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


class mySolution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # -3, 5 [5,-3, 5]
        #
        # Kadane's algorithm, exclude the "most" negative number subarray
        # if max subarray is non-circular, regular kadane's will solve
        # if max subarray is circular (wraps the end of the array), then the excluded subarray will be the MINIUM sum
        # we find the max subarray sum for a circular portion by excluding the MOST NEGATIVE non-circular portion

        # track total sum, regular max subarray sum, and min subarray sum
        total_sum = 0
        curr_max = float('-inf')
        global_max = float('-inf')
        curr_min = float('inf')
        global_min = float('inf')
        circ_max = float('-inf')
        for n in nums:
            # standard kadane's
            curr_max = max(curr_max + n, n)
            global_max = max(global_max, curr_max)

            # get minimum subarray sum
            curr_min = min(curr_min + n, n)
            global_min = min(global_min, curr_min)

            # new: get max circular sum by comparing global_max vs total-global_min
            total_sum += n
            # edge case: if nums is all negative, then total-global_min would not give valid
            if global_max > 0:
                circ_max = max(global_max, total_sum - global_min)
            else:
                circ_max = global_max

        return circ_max


class testcase1:
    nums = [1, -2, 3, -2]
    output = 3

class testcase2:
    nums = [5, -3, 5]
    output = 10

class testcase3:
    nums = [-3, -2, -3]
    output = -2

if __name__ == "__main__":
    # create Solution instance
    soln = Solution()

    # test example 1
    result1 = soln.maxSubarraySumCircular(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.maxSubarraySumCircular(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.maxSubarraySumCircular(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")