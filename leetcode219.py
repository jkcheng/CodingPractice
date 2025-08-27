# 219. Contains Duplicate II
# Easy
# Topics
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        return


class mySolution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # use hash table to store values and indices
        indices = {}

        for i, n in enumerate(nums):
            if n in indices:
                if abs(indices[n] - i) <= k:
                    return True

            indices[n] = i

        return False

class mySolution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window: maintain window of size k
        l = 0
        seen = set()

        for r, n in enumerate(nums):
            # remove leftmost value from set to maintain window
            if r - l > k:
                seen.remove(nums[l])
                l += 1

            if n in seen:
                return True

            # add new value to window
            seen.add(n)

        return False

class testcase1:
    nums = [1, 2, 3, 1]
    k = 3

class testcase2:
    nums = [1, 0, 1, 1]
    k = 1

class testcase3:
    nums = [1, 2, 3, 1, 2, 3]
    k = 2