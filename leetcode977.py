# 977. Squares of a Sorted Array
# Solved
# Easy
# Topics
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
#
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
#
#
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # get first +ve element
        start = 0
        flag = False
        for i in range(len(nums)):
            if nums[i] >= 0:
                start = i
                flag = True
                break
        if not flag:
            start = len(nums)
        negarr = nums[:start]

        posarr = nums[start:]
        for i in range(len(negarr)):
            negarr[i] = negarr[i] * negarr[i]

        for i in range(len(posarr)):
            posarr[i] = posarr[i] * posarr[i]

        negarr.reverse()

        i = 0
        j = 0
        ans = []
        while i < len(negarr) and j < len(posarr):
            if posarr[j] < negarr[i]:
                ans.append(posarr[j])
                j += 1
            else:
                ans.append(negarr[i])
                i += 1

        while i < len(negarr):
            ans.append(negarr[i])
            i += 1
        while j < len(posarr):
            ans.append(posarr[j])
            j += 1

        return ans


class mySolution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find start of negative and positive portions of array
        neg = None
        pos = None
        for i, n in enumerate(nums):
            if n < 0 and neg is None:
                neg = i
            if n >= 0 and pos is None:
                pos = i

        # reverse negative portion, handle possibly no negative or positive sections
        # [-5,-4,-2,-1]
        # [0,1,3,4]
        # [-2,-1,0,1,2]
        if neg is not None and pos is not None:
            new = nums[neg:pos][::-1]
            new.extend(nums[pos:])
        elif neg is not None and pos is None:
            new = nums[::-1]
        else:
            new = nums

        for i, n in enumerate(new):
            new[i] = n ** 2

        # merge sort if necessary
        if neg is not None and pos is not None:
            pstart = pos
            res = []
            while neg < pstart or pos < len(nums):
                if new[neg] <= new[pos]:
                    res.append(new[neg])
                    neg += 1
                else:
                    res.append(new[pos])
                    pos += 1
                # i += 1

            if pos < len(nums):
                res.extend(new[pos:])
            else:
                res.extend(new[neg:pstart])
        else:
            res = new
        return res

class testcase1:
    nums = [-4, -1, 0, 3, 10]

class testcase2:
    nums = [-7, -3, 2, 3, 11]

class testcase3:
    nums = [-7, -3, -1]

class testcase4:
    nums = [1, 3, 7]

class testcase5:
    nums = [-5,-4, 10, 20]

class testcase6:
    nums = [-10000, -9999, -7, -5, 0, 0, 10000]

class testcase7:
    nums = [-2,0]