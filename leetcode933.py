# 933. Number of Recent Calls
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You have a RecentCounter class which counts the number of recent requests within a certain time frame.
#
# Implement the RecentCounter class:
#
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
#
#
#
# Example 1:
#
# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]
#
# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
#
#
# Constraints:
#
# 1 <= t <= 109
# Each test case will call ping with strictly increasing values of t.
# At most 104 calls will be made to ping.

from typing import List, Optional

from collections import deque
class RecentCounter:

    def __init__(self):
        self.calls = deque()

    def ping(self, t):
        self.calls.append(t)
        while self.calls[0] < self.calls[-1] - 3000:
            self.calls.popleft()
        return len(self.calls)


class myRecentCounter:

    def __init__(self):
        # create queue to maintain requests with value t - 3000
        # self.queue = []

        # can use deque for optimization
        self.queue = deque()
        return

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            # self.queue.pop(0) # regular list
            self.queue.popleft() # deque


        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

class testcase1:
    input = ["RecentCounter", "ping", "ping", "ping", "ping"]
    inputvals = [[], [1], [100], [3001], [3002]]
    output = [None, 1, 2, 3, 3]


if __name__ == "__main__":
    # create Solution instance
    soln = myRecentCounter()

    # test example 1
    result1 = []
    for input in testcase1.inputvals:
        if len(input) > 0:
            r = soln.ping(input[0])
        else:
            r = None
        result1.append(r)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

