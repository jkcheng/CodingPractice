# 42. Trapping Rain Water
# Solved
# Hard
# Topics
# Array
# Two Pointers
# Monotonic Stack
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
#
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

#

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, 0
        # start pointers at left and right ends of array
        l, r = 0, len(height) - 1

        water = 0
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax < rmax:  # calculate water at position l
                water += lmax - height[l]
                l += 1
            else:
                water += rmax - height[r]
                r -= 1

        return water


class mySolution:
    def trap(self, height: List[int]) -> int:
        # O(n), build monotonic stack of highest where left[i] is highest height seen from left and right[i] is
        # highest height seen from right. Then scan array again and calculate rainwater as min(left[i],right[i])-height[i]

        # build monotonic stack from left
        left = []
        highest = 0
        for i,h in enumerate(height):
            highest = max(highest,h)
            left.append(highest)

        # monotonic stack from right
        right = [0]*len(height)
        highest = 0
        for i in reversed(range(len(height))):
            highest = max(highest,height[i])
            right[i] = highest

        # calculate rainwater depth
        depths = []
        for i,h in enumerate(height):
            depth = min(left[i],right[i]) - height[i]
            depths.append(depth)

        return sum(depths)


class testcase1:
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

class testcase2:
    height = [4, 2, 0, 3, 2, 5]