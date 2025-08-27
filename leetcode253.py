# 253. Meeting Rooms II
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class mySolution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # line sweep, dictionary version
        # timeline = [0]*10**6
        timeline = {}
        for i in intervals:
            timeline[i.start] = timeline.get(i.start, 0) + 1
            timeline[i.end] = timeline.get(i.end, 0) - 1

        meetings = 0
        minrooms = 0
        for i in sorted(timeline.keys()):
            meetings += timeline[i]
            minrooms = max(minrooms, meetings)

        return minrooms


class mySolution2:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # line sweep, array solution
        timeline = [0] * 10 ** 6
        for i in intervals:
            timeline[i.start] += 1
            timeline[i.end] -= 1

        meetings = 0
        minrooms = 0
        for t in timeline:
            meetings += t
            minrooms = max(minrooms, meetings)

        return minrooms

class testcase1:
    intervalarray = [[0, 30],[5, 10],[15, 20]]
    intervals = [Interval(i[0],i[1]) for i in intervalarray]

class testcase1:
    intervalarray = [[7, 10], [2, 4]]
    intervals = [Interval(i[0],i[1]) for i in intervalarray]