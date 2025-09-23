# 149. Max Points on a Line
# Hard
# Topics
# premium lock icon
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
#
#
#
# Example 1:
#
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:
#
#
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
#
#
# Constraints:
#
# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.

from typing import List, Optional


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        return


class mySolution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # use intercept to handle different lines with same slope
        # line unique indicator: slope and intercept
        # calculate slope + intercept of each pair of points, add to hash table with those as key
        slopes = {}

        # edge case of single point
        if len(points) == 1:
            return 1

        for p1 in points:
            for p2 in points:
                p1 = tuple(p1)
                p2 = tuple(p2)
                # skip coordinates if they are the same
                if p1 == p2:
                    continue
                # handle infinite slope
                if p1[0] == p2[0]:
                    slope = None
                else:
                    slope = (p1[1] - p2[1]) / (p1[0] - p2[0])

                # calculate intercept
                # y = mx + c
                # c = y - mx
                if slope is not None:
                    intercept = p1[1] - slope * p1[0]
                else:
                    intercept = p1[0]

                # add to dict
                key = (slope, intercept)
                line_points = slopes.get(key, set())
                line_points.add(p1)
                line_points.add(p2)
                slopes[key] = line_points

        ans = 0
        for line_points in slopes.values():
            ans = max(ans, len(line_points))

        print(slopes)
        return ans


class testcase1:
    points = [[1,1],[2,2],[3,3]]
    output = 3

class testcase2:
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    output = 4

class testcase3:
    points = [[0,0]]
    output = 1

class testcase4:
    points = [[3,3],[1,4],[1,1],[2,1],[2,2]]
    output = 3


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.maxPoints(testcase1.points)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.maxPoints(testcase2.points)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.maxPoints(testcase3.points)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.maxPoints(testcase4.points)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")