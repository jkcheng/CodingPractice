# 2462. Total Cost to Hire K Workers
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
#
# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:
#
# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.
#
#
#
# Example 1:
#
# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.
# Example 2:
#
# Input: costs = [1,2,4,1], k = 3, candidates = 3
# Output: 4
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
# - In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
# - In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
# The total hiring cost is 4.
#
#
# Constraints:
#
# 1 <= costs.length <= 105
# 1 <= costs[i] <= 105
# 1 <= k, candidates <= costs.length

from typing import List, Optional

import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q = costs[:candidates]
        qq = costs[max(candidates, len(costs)-candidates):]
        heapify(q)
        heapify(qq)
        ans = 0
        i, ii = candidates, len(costs)-candidates-1
        for _ in range(k):
            if not qq or q and q[0] <= qq[0]:
                ans += heappop(q)
                if i <= ii:
                    heappush(q, costs[i])
                    i += 1
            else:
                ans += heappop(qq)
                if i <= ii:
                    heappush(qq, costs[ii])
                    ii -= 1
        return ans


import heapq
class mySolution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # O(klogcandidates)? priority queue using min heap
        # create two min heaps for left/right of candidates using cost and index values
        # compare top of heaps and pop lowest value k times to update cost
        # replace appropriate heap with the next worker
        # return total cost

        # get candidates
        leftworkers = costs[:candidates]
        rightworkers = costs[max(candidates, len(costs) - candidates):]  # handle candidates larger than half of costs
        heapq.heapify(leftworkers)
        heapq.heapify(rightworkers)

        # pop candidates from queue and maintain queue size
        totalcost = 0
        nextleft = candidates
        nextright = max(candidates - 1, len(costs) - candidates - 1)
        while k > 0:
            # pop lowest cost candidate and update total cost
            if len(rightworkers) == 0 or (len(leftworkers) > 0 and leftworkers[0] <= rightworkers[0]):
                cost = heapq.heappop(leftworkers)
                totalcost += cost
                # make sure costs[nextleft] isn't already in the right heap
                if nextleft <= nextright:
                    heapq.heappush(leftworkers, costs[nextleft])
                    nextleft += 1
            else:  # leftworkers is empty or leftworkers[0] is not less than rightworkers[0]
                cost = heapq.heappop(rightworkers)
                totalcost += cost
                if nextleft <= nextright:
                    heapq.heappush(rightworkers, costs[nextright])
                    nextright -= 1

            k -= 1

        return totalcost


class testcase1:
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4
    output = 11

class testcase2:
    costs = [1, 2, 4, 1]
    k = 3
    candidates = 3
    output = 4


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.totalCost(testcase1.costs, testcase1.k, testcase1.candidates)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.totalCost(testcase2.costs, testcase2.k, testcase2.candidates)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")