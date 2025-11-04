# 1004. Max Consecutive Ones III
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:
#
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

from typing import List, Optional


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = right = 0

        for right in range(len(A)):
            # if we encounter a 0 the we decrement K
            if A[right] == 0:
                K -= 1
            # else no impact to K

            # if K < 0 then we need to move the left part of the window forward
            # to try and remove the extra 0's
            if K < 0:
                # if the left one was zero then we adjust K
                if A[left] == 0:
                    K += 1
                # regardless of whether we had a 1 or a 0 we can move left side by 1
                # if we keep seeing 1's the window still keeps moving as-is
                left += 1

        return right - left + 1


class mySolution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # O(n), sliding window, grow window when 1's are encountered
        # include 0's up to k number
        # when 0 encountered after k 0's already included, shrink left edge of window
        # shrink left edge until enough less than k 0's remaining in window
        # grow window again until end of nums

        l, r = 0, 0
        maxwindow = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and k > 0:  # including a zero
                r += 1
                k -= 1
            elif nums[r] == 0 and k == 0:  # shrink left edge
                while k == 0:
                    if nums[l] == 0:  # check if zero to be removed
                        k += 1
                    l += 1

            # track max window length
            maxwindow = max(maxwindow, r - l)

        return maxwindow

class testcase1:
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    output = 6

class testcase2:
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    output = 10


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.longestOnes(testcase1.nums, testcase1.k)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.longestOnes(testcase2.nums, testcase2.k)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")