# 11. Container With Most Water
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
#
#
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        return

class mySolution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n), two pointers, move pointer at shorter height inward
        l, r = 0, len(heights) - 1
        maxarea = 0
        while l < r:
            # check area at current pointers, store largest area seen
            area = (r - l) * min(heights[l], heights[r])
            maxarea = max(maxarea, area)

            # move pointer with lower height
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxarea

class testcase1:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

class testcase2:
    height = [1, 1]