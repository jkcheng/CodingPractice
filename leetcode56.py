# 56. Merge Intervals
# Solved
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
# Constraints:
#
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        return


class mySolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by interval start value
        # iterate through intervals and merge when intervals[n][0] <= intervals[n-1][1]

        # sort intervals by start
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        prev = 0
        for i in range(len(intervals)):
            if i > 0:
                # merge intervals if start <= previous end
                if intervals[i][0] <= intervals[prev][1]:
                    intervals[prev][1] = max(intervals[prev][1], intervals[i][1])
                else:  # add previous interval to ans
                    ans.append(intervals[prev])
                    prev = i

        # add final interval
        ans.append(intervals[prev])
        return ans

class testcase1:
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    output = [[1,6],[8,10],[15,18]]

class testcase2:
    intervals = [[1, 4], [4, 5]]
    output = [[1,5]]

class testcase3:
    intervals = [[1,3],[2,6],[6,10],[10,18]]
    output = [[1,18]]

class testcase4:
    intervals = [[1, 4], [2, 3], [8, 10]]
    output = [[1, 4], [8, 10]]
