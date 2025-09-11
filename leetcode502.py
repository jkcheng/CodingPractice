# 502. IPO
# Hard
# Topics
# premium lock icon
# Companies
# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.
#
# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.
#
# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
#
# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.
#
# The answer is guaranteed to fit in a 32-bit signed integer.
#
#
#
# Example 1:
#
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
# Example 2:
#
# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6
#
#
# Constraints:
#
# 1 <= k <= 105
# 0 <= w <= 109
# n == profits.length
# n == capital.length
# 1 <= n <= 105
# 0 <= profits[i] <= 104
# 0 <= capital[i] <= 109

from typing import List, Optional


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:


        return

# TLE: O(knlogn)
import heapq
class mySolution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # use heap to maintain a collection of elligible projects
        # pop largest profit project out of heap k times
        # runtime: knlogn?

        # get list of elligible projects and place into heap
        zipped = [(p, c) for p, c in zip(profits, capital)]
        heap = []
        # create set of projects already elligible
        heaped = set()
        for i, vals in enumerate(zipped):
            if i not in heaped and vals[1] <= w:
                heap.append(-vals[0])  # negative values for max heap in python
                heaped.add(i)

        heapq.heapify(heap)

        # repeatedly pick project and update heap
        while k > 0:
            if len(heap) > 0:
                w += -1 * heapq.heappop(heap)  # heap profit value are negative
                # update heap with new projects using new w value
                for i, vals in enumerate(zipped):
                    if i not in heaped and vals[1] <= w:
                        heapq.heappush(heap, -vals[0])  # negative values for max heap in python
                        heaped.add(i)

                k -= 1
            else:  # no elligible projects left
                break

        return w

import heapq
class mySolution2:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # use heap to maintain a collection of elligible projects
        # pop largest profit project out of heap k times
        # runtime: nlogn ?

        # get list of elligible projects and place into heap
        zipped = [(p, c) for p, c in zip(profits, capital)]
        heap = []
        # optimization: sort project list and use pointer to indicate elligibility
        projects = sorted(zipped, key=lambda x: x[1])  # sort by increasing capital

        # repeatedly pick project and update heap
        i = 0
        while k > 0:
            while i < len(projects) and projects[i][1] <= w:
                # push elligible project to heap
                heapq.heappush(heap, -1 * projects[i][0])  # heap profit value are negative
                i += 1

            # pop project with largest profit if available
            if len(heap) > 0:
                w += -1 * heapq.heappop(heap)
            k -= 1

        return w


class testcase1:
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    output = 4

class testcase2:
    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    output = 6

class testcase3:
    k = 10
    w = 0
    profits = [1,2,7,9]
    capital = [0,1,1,100]
    output = 10


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.findMaximizedCapital(testcase1.k, testcase1.w, testcase1.profits, testcase1.capital)
    print(f"Example 1 - Expected: {testcase1.capital[-1]}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.findMaximizedCapital(testcase2.k, testcase2.w, testcase2.profits, testcase2.capital)
    print(f"Example 2 - Expected: {testcase2.capital[-1]}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.findMaximizedCapital(testcase3.k, testcase3.w, testcase3.profits, testcase3.capital)
    print(f"Example 3 - Expected: {testcase3.capital[-1]}, Got: {result3}, Correct: {testcase3.output == result3}")