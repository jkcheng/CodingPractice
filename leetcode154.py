# 154. Find Minimum in Rotated Sorted Array II
# Solved
# Hard
# Topics
# Companies
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
#
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
#
# You must decrease the overall operation steps as much as possible.
#
#
#
# Example 1:
#
# Input: nums = [1,3,5]
# Output: 1
# Example 2:
#
# Input: nums = [2,2,2,0,1]
# Output: 0
#
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
#
#
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
#
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # [4,4]
        # [4,7,4]
        # [4,1,4]
        # [4,4,4,1,2,4]
        # [4,1,4,4,4]
        # [4,4,4,4,4]

        # [4,4,0,1,2,4]
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) // 2
            # if nums[mid] > nums[hi]:
            #     lo = mid + 1
            # else:
            #     hi = mid if nums[hi] != nums[mid] else hi - 1
            # print('lo:', lo, 'hi:', hi, 'mid:', mid)
            if nums[mid] > nums[hi]: # mid in bigger half, minimum to the right
                lo = mid + 1
                # print('lo = mid + 1')
            elif nums[mid] != nums[hi]: # mid < nums[hi], minimum to the left
                hi = mid
                # print('hi = mid')
            else: # ambiguous case, shrink search range by one element on the right and search again
                hi -= 1
                # print('hi -= 1')
        return nums[lo]

# O(logn): average case, not worst case. Worst case still O(n) due to duplicates allowed and special case of
# nums[l] == nums[mid] == nums[r]. Impossible to determine which half does not contain the minimum and can be eliminated.
class mySolution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        minval = float('inf')
        while l <= r:
            mid = (l+r)//2
            # minimum to the right, mid in larger half
            # compare to nums[r] instaed of nums[-1] because of else statement decreasing search space by 1
            if nums[mid] > nums[r]:
                l = mid+1
            # minimum to the left, mid in smaller half OR perfectly sorted array
            elif nums[mid] < nums[0] or nums[mid] > nums[0]:
                minval = min(minval, nums[mid])
                r = mid-1
            # ambiguous, minimum could be left or right, decrease search space by 1
            # nums[mid] == nums[0]
            else:
                minval = min(minval, nums[mid])
                r -= 1

        return minval

class testcase1:
    nums = [1,3,5]

class testcase2:
    nums = [2,2,2,0,1]

class testcase3:
    nums = [2,2,2,2,1]

class testcase4:
    nums = [4,4,4,4,4,4]

class testcase5:
    nums = [4,4,2,2,2,2]

class testcase6:
    nums = [3,3,1,3]