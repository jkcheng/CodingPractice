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

from leetcode1 import testcase3


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]

# using heap, heapify negative of nums, then pop k times to get kth largest
# time complexity: O(nlogk)
import heapq
class mySolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        while k > 0:
            num = heapq.heappop(heap)
            k -= 1
        return -num

# using quickselect, n run time on average
# choose a pivot value at random, then partition array into greater than, less than, equal partitions
# recursively search correct partition until we know kth largest element is in the equal partition
# if k <= len([larger_values]), recurse searching on larger partition
# if k > len([larger + equal]), recurse searching on smaller partition
# else, kth largest is in equal partition
import random
class mySolution2:
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


class testcase1:
    nums = [3,2,1,5,6,4]
    k = 2
    output = 5

class testcase2:
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    output = 4

class testcase3:
    nums = [1]
    k = 1
    output = 1

# ai generated
class testcase4:
    nums = [1,2,3,4,5,6,7,8,9,10]
    k = 1
    output = 10

class testcase5:
    nums = [1,2,3,4,5,6,7,8,9,10]
    k = 10
    output = 1


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.findKthLargest(testcase1.nums, testcase1.k)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.findKthLargest(testcase2.nums, testcase2.k)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.findKthLargest(testcase3.nums, testcase3.k)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.findKthLargest(testcase4.nums, testcase4.k)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.findKthLargest(testcase5.nums, testcase5.k)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")