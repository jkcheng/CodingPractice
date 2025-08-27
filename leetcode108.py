# 108. Convert Sorted Array to Binary Search Tree
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
#
#
#
# Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
# Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

from typing import List,Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return


class mySolution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # middle value of array will be root
        # divide and conquer: recursively split array in half
        # recurse on left/right half of array

        def recurse(nums):
            # check if nums is empty
            if len(nums) == 0:
                return None

            right = len(nums)-1
            left = 0
            mid = (left+right)//2

            root = TreeNode(nums[mid])
            root.left = recurse(nums[0:mid])
            if len(nums) > 1:
                root.right = recurse(nums[mid+1:])

            return root

        return recurse(nums)


class testcase1:
    nums = [-10,-3,0,5,9]
    output = [0,-3,9,-10,None,5]

class testcase2:
    nums = [1,3]
    output = [3,1]

# ai generated
class testcase3:
    nums = [1,3,None,None,2]
    output = [3,1,None,None,2]

class testcase4:
    nums = [3,1,4,None,None,2]
    output = [3,1,4,None,None,2]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.sortedArrayToBST(testcase1.nums)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.sortedArrayToBST(testcase2.nums)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.sortedArrayToBST(testcase3.nums)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.sortedArrayToBST(testcase4.nums)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")