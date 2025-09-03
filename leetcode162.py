# 162. Find Peak Element
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# A peak element is an element that is strictly greater than its neighbors.
#
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

from typing import List, Optional

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while(left < right):
            # mid = left +(right-left)//2 # avoid int overflow
            mid = (left + right)//2
            if nums[mid] <  nums[mid+1]: # False Condition # inc function # go right # Find First False
                # i.e. find First elem when this if will be false
                left = mid+1 # exclude mid
            else:
                right = mid
        return left


class mySolution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search, search side with increasing neighbor
        # if both are increasing, choose one arbitrarily because a peak is guaranteed in that direction?
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2  # (l + (r-l))//2 to avoid overflow
            # return index if at peak
            # if mid+1 < len(nums) and nums[mid+1] < nums[mid] and mid-1 > -1 and nums[mid-1] < nums[mid] :
            if (mid + 1 >= len(nums) or nums[mid + 1] < nums[mid]) and (mid - 1 < 0 or nums[mid - 1] < nums[mid]):
                return mid
            # search right if value is greater
            elif mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1


class testcase1:
    nums = [1,2,3,1]
    output = [2]

class testcase2:
    nums = [1,2,1,3,5,6,4]
    output = [5,1]

# ai generated + edited
class testcase3:
    nums = [1,2,3,1,2,1]
    output = [2,4]

class testcase4:
    nums = [1,2,1,3,5,6,4,1,2,1]
    output = [1,5,8]

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.findPeakElement(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 in testcase1.output}")

    # test example 2
    result2 = soln.findPeakElement(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 in testcase2.output}")

    # test example 3
    result3 = soln.findPeakElement(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 in testcase3.output}")

    # test example 4
    result4 = soln.findPeakElement(testcase4.nums)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 in testcase4.output}")