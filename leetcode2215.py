# 2215. Find the Difference of Two Arrays
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
#
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
#
#
#
# Example 1:
#
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
# Example 2:
#
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
#
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000

from typing import List, Optional


class Solution:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]


class mySolution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # O(m+n), create sets from nums1, nums2, then iterate through sets and check existence in other set

        # create sets
        set1 = set(nums1)
        set2 = set(nums2)

        # check existence
        answer = [[], []]
        for n in set1:
            if n not in set2:
                answer[0].append(n)

        for n in set2:
            if n not in set1:
                answer[1].append(n)

        return answer


class testcase1:
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    output = [[1,3],[4,6]]

class testcase2:
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    output = [[3],[]]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.findDifference(testcase1.nums1, testcase1.nums2)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.findDifference(testcase2.nums1, testcase2.nums2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")