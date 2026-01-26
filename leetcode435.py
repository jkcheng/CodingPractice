# 435. Non-overlapping Intervals
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
#
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
#
#
#
# Example 1:
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:
#
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:
#
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
#
#
# Constraints:
#
# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104

from typing import List, Optional

# https://leetcode.com/problems/non-overlapping-intervals/solutions/793070/python-on-log-n-sort-ends-with-proof-exp-0q2k
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n, count = len(intervals), 1
        if n == 0: return 0
        curr = intervals[0]

        for i in range(n):
            if curr[1] <= intervals[i][0]:
                count += 1
                curr = intervals[i]

        return n - count


class mySolution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(nlogn), sort asc by start, build stack and remove intervals that are overlapping
        # when two intervals overlap, keep shorter interval by comparing end time

        intervals = sorted(intervals, key=lambda x: (x[0], x[1])) # key is actually default sorting behavior

        # build stack of non-overlapping intervals
        stack = []
        count = 0
        for i in intervals:
            if len(stack) > 0 and stack[-1][1] > i[0]:
                count += 1
                # keep shorter interval
                if i[1] < stack[-1][1]:
                    stack.pop()
                    stack.append(i)
            else:
                stack.append(i)

        return count


class testcase1:
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    output = 1

class testcase2:
    intervals = [[1, 2], [1, 2], [1, 2]]
    output = 2

class testcase3:
    intervals = [[1, 2], [2, 3]]
    output = 0

class testcase4:
    intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
    output = 7


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.eraseOverlapIntervals(testcase1.intervals)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.eraseOverlapIntervals(testcase2.intervals)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.eraseOverlapIntervals(testcase3.intervals)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.eraseOverlapIntervals(testcase4.intervals)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")