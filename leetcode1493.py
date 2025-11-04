# 1493. Longest Subarray of 1's After Deleting One Element
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
#
#
#
# Example 1:
#
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:
#
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:
#
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

from typing import List, Optional


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        return


class mySolution:
    def longestSubarray(self, nums: List[int]) -> int:
        # O(n), sliding window, find largest window with at most 1x zero and return length-1
        # extend right edge when encountering 1 or at most one 0
        # if num zeros > 1, then move window and num zeros inside
        # extend window right edge again if num zeros inside < 1

        l, r = 0, 0
        maxwindow = 0
        numzero = 0
        for r in range(len(nums)):
            # track number of zeros in window
            if nums[r] == 0:
                numzero += 1

            # if window expansion not allowed, move left edge
            if numzero > 1:
                if nums[l] == 0:
                    numzero -= 1
                l += 1

        return r - l


class testcase1:
    nums = [1,1,0,1]
    output = 3

class testcase2:
    nums = [0,1,1,1,0,1,1,0,1]
    output = 5

class testcase3:
    nums = [1,1,1]
    output = 2


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.longestSubarray(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.longestSubarray(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.longestSubarray(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")