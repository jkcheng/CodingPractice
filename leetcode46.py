# 46. Permutations
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
#
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
#
# Input: nums = [1]
# Output: [[1]]
#
#
# Constraints:
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

from typing import List, Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(nums, p, n):
            # update permutation
            p.append(n)
            newnums = nums.copy()
            newnums.remove(n)

            if len(newnums) == 0:
                ans.append(p)
                return

            for n in newnums:
                backtrack(newnums.copy(), p.copy(), n)

        for n in nums:
            backtrack(nums.copy(), [], n)

        return ans


class mySolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack, O(n^2): create recursive function to iterate through nums
        # turn nums into set (values are unique)
        # itereate through each n in nums, remove n from set, then recurse on rest of set

        def backtrack(nums, n, curr): #
            # add n to current permutation
            curr.append(n)

            # remove n from a copy of nums
            nums_copy = nums.copy()
            nums_copy.remove(n)

            # add permutation if nums is empty
            if len(nums_copy) == 0:
                ans.append(curr)
                return

            # iterate through items of copy
            for othern in nums_copy:
                backtrack(nums_copy, othern, curr.copy())

        ans = []
        nums = set(nums)
        for n in nums:
            curr = []
            backtrack(nums, n, curr)

        return ans


class testcase1:
    nums = [1, 2, 3]
    output = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

class testcase2:
    nums = [0, 1]
    output = [[0, 1], [1, 0]]

class testcase3:
    nums = [1]
    output = [[1]]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.permute(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.permute(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.permute(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")