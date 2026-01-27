# 452. Minimum Number of Arrows to Burst Balloons
# Solved
# Medium
# Topics
# Companies
# There are some spherical balloons taped onto a flat wall that represents the XY-plane.
# The balloons are represented as a 2D integer array points where points[i] = [xstart, xend]
# denotes a balloon whose horizontal diameter stretches between xstart and xend.
# You do not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely,
# bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
#
#
#
# Example 1:
#
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
# Example 2:
#
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
# Example 3:
#
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
#
#
# Constraints:
#
# 1 <= points.length <= 105
# points[i].length == 2
# -231 <= xstart < xend <= 231 - 1

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        return


class mySolution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # merge ranges and find number of non-overlapping ranges
        # sort ranges by start, count arrows only if new range does not overlap previous
        points = sorted(points, key=lambda x: x[1])

        prev = 0
        arrows = 1
        for i in range(len(points)):
            if i > 0:
                point = points[i]
                prev_point = points[prev]

                # check for nonoverlap
                if point[0] > prev_point[1]:
                    arrows += 1
                    prev = i

        return arrows

class mySolution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # interval problem, detect overlapping intervals
        # O(nlogn), sort + count overlapping intervals
        # start balloon with leftmost ending and remove any overlapping balloons from consideration
        # increment arrows for first non-overlapping balloon and use this new balloon for overlap detection

        points = sorted(points, key=lambda x: x[1])
        arrows = 1

        curr = points[0]
        for balloon in points:
            # new non-overlapping balloon, increment curr and arrows
            if balloon[0] > curr[1]:
                curr = balloon
                arrows += 1

        return arrows

class testcase1:
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    output = 2

class testcase2:
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    output = 4

class testcase3:
    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    output = 2

class testcase4:
    points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
    output = 2


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.findMinArrowShots(testcase1.points)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.findMinArrowShots(testcase2.points)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.findMinArrowShots(testcase3.points)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.findMinArrowShots(testcase4.points)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")