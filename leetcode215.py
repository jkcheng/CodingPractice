# 215. Kth Largest Element in an Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
#
#
#
# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

from typing import List, Optional

# https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/1019513/python-quickselect-average-on-explained-mizjp
# using quickselect, n run time on average
# choose a pivot value at random, then partition array into greater than, less than, equal partitions
# recursively search correct partition until we know kth largest element is in the equal partition
# if k <= len([larger_values]), recurse searching on larger partition
# if k > len([larger + equal]), recurse searching on smaller partition
# else, kth largest is in equal partition
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # choose random pivot
        pivot = random.choice(nums)

        # split nums into greater, equal, smaller, partitions
        greater = [n for n in nums if n > pivot]
        equal = [n for n in nums if n == pivot]
        smaller = [n for n in nums if n < pivot]

        # recurse on correct partition
        glen, elen = len(greater), len(equal)
        if k <= glen: # kth largest in greater partition
            return self.findKthLargest(greater, k)
        elif k > (glen + elen): # kth largest in smaller partition
            # kth largest will become (k - glen - elen)th largest
            return self.findKthLargest(smaller, k - glen - elen)
        else:
            return equal[0]

# using heapq
import heapq
class mySolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(nlogk), create heap and pop k elements out of array

        # create heap
        heap = [-1 * n for n in nums]
        heapq.heapify(heap)

        # pop top k items
        while k > 0:
            val = heapq.heappop(heap)
            k -= 1

        return -val


class testcase1:
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    output = 5

class testcase2:
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    output = 4


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.findKthLargest(testcase1.nums, testcase1.k)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.findKthLargest(testcase2.nums, testcase2.k)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")