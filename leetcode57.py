# 57. Insert Interval
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
# intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
#
#
#
# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        return

class mySolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iterate over intervals and handle 3 cases:
        # 1. newInterval is after otherInterval, simply append other interval
        # 2. newInterval overlaps otherInterval, merge newInterval with otherInterval (key: reuse this newly merged newInterval for comparisons)
        # 3. newInterval is before otherInterval, append newInterval
        ans = []
        added = False
        for other in intervals:
            # 1. newInterval is after other
            if newInterval[0] > other[1]:
                ans.append(other)
            # 2. new interval overlaps other
            # newInterval[0] <= other[1] already implied by previous if condition
            # need to check the other range values to ensure overlapping
            elif newInterval[1] >= other[0]:
                newInterval[0] = min(newInterval[0], other[0])
                newInterval[1] = max(newInterval[1], other[1])
            # # 3. newInterval is before other
            else:
                if added is False:
                    ans.append(newInterval)
                    added = True
                ans.append(other)

        # handle empty intervals
        if added is False:
            ans.append(newInterval)

        return ans

class aiSolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Initialize result list
        result = []

        # Edge case: empty intervals
        if not intervals:
            return [newInterval]

        # Initialize new interval start and end
        new_start, new_end = newInterval

        # Flag to track if we've inserted the new interval
        inserted = False

        for interval in intervals:
            # Current interval is completely before new interval
            if interval[1] < new_start:
                result.append(interval)
            # Current interval is completely after new interval
            elif interval[0] > new_end:
                # If we haven't inserted the new interval yet, do it now
                if not inserted:
                    result.append([new_start, new_end])
                    inserted = True
                result.append(interval)
            # Current interval overlaps with new interval
            else:
                # Update new interval boundaries
                new_start = min(new_start, interval[0])
                new_end = max(new_end, interval[1])

        # If we haven't inserted the new interval yet, do it now
        if not inserted:
            result.append([new_start, new_end])

        return result

class aiSolution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Initialize three lists for intervals before, overlapping, and after the new interval
        before = []
        after = []

        # Process each interval
        for interval in intervals:
            # Current interval ends before new interval starts
            if interval[1] < newInterval[0]:
                before.append(interval)
            # Current interval starts after new interval ends
            elif interval[0] > newInterval[1]:
                after.append(interval)
            # Current interval overlaps with new interval
            else:
                # Update new interval boundaries
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # Combine the three lists
        return before + [newInterval] + after

# Test cases
class testcase1:
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    output = [[1,5],[6,9]]

class testcase2:
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    output = [[1,2],[3,10],[12,16]]

class testcase3:
    intervals = [[2,3]]
    newInterval = [1, 10]
    output = [[1, 10]]

# ai generated
class testcase4:
    intervals = []
    newInterval = [5,7]
    output = [[5,7]]

class testcase5:
    intervals = [[1,5]]
    newInterval = [2,3]
    output = [[1,5]]

class testcase6:
    intervals = [[1,5]]
    newInterval = [6,8]
    output = [[1,5],[6,8]]

# Test the solution
if __name__ == "__main__":
    # Create solution instance
    solution = mySolution()

    # Test with example 1
    result1 = solution.insert(testcase1.intervals, testcase1.newInterval)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # Test with example 2
    result2 = solution.insert(testcase2.intervals, testcase2.newInterval)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # Test with empty intervals
    result3 = solution.insert(testcase3.intervals, testcase3.newInterval)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # Test with contained interval
    result4 = solution.insert(testcase4.intervals, testcase4.newInterval)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # Test with interval after all existing
    result5 = solution.insert(testcase5.intervals, testcase5.newInterval)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")
