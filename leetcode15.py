# 15. 3Sum
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
#
# Constraints:
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# https://leetcode.com/problems/3sum/solutions/7498/python-solution-with-detailed-explanation

from typing import List

# sorting pointer solution with duplicate checks for speed optimization
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        # only iterate to the second-last element since we need a minimum of three elements in solution
        for i in range(len(nums)-2):
            first =  nums[i]

            # two sum pointer solution for sorted array
            l = i+1
            r = len(nums)-1
            while l<r:
                second = nums[l]
                third = nums[r]
                candidate = first + second + third
                if candidate == 0:
                    # because nums is in sorted order, each solution triplet encountered will always be in the same order
                    ans.add((first,second,third))
                    l += 1
                    r -= 1
                    # continue increment l if nums[l] is duplicate of previous value
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    # continue decrement r if nums[r] is duplicate of previous value
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif candidate < 0:
                    l += 1
                elif candidate > 0:
                    r -= 1

        # convert back to list of list for output
        ans = [list(s) for s in ans]
        return ans


class mySolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(nlogn + n*n), sort array then iterate through array and
        # perform two-pointer 2sum solution on the rest of the sorted array
        # avoid duplicates by only considering the rest of the array, because for an arbitrary
        # value nums[i], if it is part of a triplicate it would have been discovered
        # in an earlier iteration
        nums = sorted(nums)
        ans = []

        # iterate to len(nums)-2 to exclude last two values
        for i in range(len(nums)-2):
            # duplicate check to skip to next i if same value encountered
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # two-pointer 2sum solution
            l, r = i + 1, len(nums) - 1
            while l < r:
                candidate = nums[i] + nums[l] + nums[r]
                if candidate == 0:
                    triplet = [nums[i], nums[l], nums[r]]
                    ans.append(triplet)
                    # continue checking array for pairs that could for a new triplet with nums[i]
                    l += 1
                    r -= 1
                    # duplicate handling: increment l if new nums[l] == nums[l-1]
                    # due to sorting we are guaranteed duplicate will be adjacent
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    # not strictly necessary to do the same with r, since any duplicated r would result in a duplicated l in triplet~!
                    # while l < r and nums[r] == nums[r + 1]:
                    #     r -= 1
                # increment l to find a larger candidate if sum < 0
                elif candidate < 0:
                    l += 1
                else:
                    r -= 1

        return ans

class testcase1:
    nums = [-1, 0, 1, 2, -1, -4]

class testcase2:
    nums = [0, 1, 1]

class testcase3:
    nums = [0, 0, 0]

class testcase4:
    nums = [0,0,0,0]

class testcase5:
    nums = [-2,0,1,1,2]

class testcase6:
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]