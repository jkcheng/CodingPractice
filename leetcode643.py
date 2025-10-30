# 643. Maximum Average Subarray I
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:
#
# Input: nums = [5], k = 1
# Output: 5.00000
#
#
# Constraints:
#
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

from typing import List, Optional


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize currSum and maxSum to the sum of the initial k elements
        currSum = maxSum = sum(nums[:k])

        # Start the loop from the kth element
        # Iterate until you reach the end
        for i in range(k, len(nums)):
            # Subtract the left element of the window
            # Add the right element of the window
            currSum += nums[i] - nums[i - k]

            # Update the max
            maxSum = max(maxSum, currSum)

        # Since the problem requires average, we return the average
        return maxSum / k


class mySolution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # O(n), sliding window, maintain window of length k update max average seen

        # initial total and max average
        total = sum(nums[0:k])
        maxsum = total

        # iterate through indexes k through len(nums), update max sum
        # edge case: if k == len(nums), then loop conveniently does not execute
        for i in range(k, len(nums)):
            # add new value
            total += nums[i]

            # subtract old value, starting from index 0
            total -= nums[i-k]

            # update max avg
            maxsum = max(maxsum, total)

        return maxsum / k


class testcase1:
    nums = [1,12,-5,-6,50,3]
    k = 4
    output = 12.75000

class testcase2:
    nums = [5]
    k = 1
    output = 5.00000


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.findMaxAverage(testcase1.nums, 4)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.findMaxAverage(testcase2.nums, 1)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")