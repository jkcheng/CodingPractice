# 134. Gas Station
# Solved
# Medium
# Topics
# Companies
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas
# to travel from the ith station to its next (i + 1)th station.
# You begin the journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station's index
# if you can travel around the circuit once in the clockwise direction, otherwise return -1.
# If there exists a solution, it is guaranteed to be unique.
#
#
#
# Example 1:
#
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:
#
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.
#
#
# Constraints:
#
# n == gas.length == cost.length
# 1 <= n <= 105
# 0 <= gas[i], cost[i] <= 104

# https://leetcode.com/problems/gas-station/solutions/42568/share-some-of-my-ideas
# https://leetcode.com/problems/gas-station/solutions/860347/python-simple-and-very-short-explained-solution-o-n-o-1-faster-than-98
# https://leetcode.com/problems/gas-station/solutions/860347/python-simple-and-very-short-explained-solution-o-n-o-1-faster-than-98/comments/2505553/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return


class mySolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # O(n), if sum(gas) >= sum(cost), then there must be a solution
        # for an arbitrary station A, if B is the FIRST station that is unreachable then all stations
        # between A and B (C..Ck) must also be reachable by A (and thus cannot reach B)
        # thus we can simply restart at B and check if we can reach the end of the array and B will be the solution
        # because we are guaranteed that a solution exists and is unique.
        # We B can form a loop because we previously verified there is enough gas in the entire array to make a loop,
        # and the sum of gas from B -> array end has enough gas, so sum of gas from array start to B should have enough
        # for the entire loop trip

        # verify that a solution exists
        if sum(gas) < sum(cost):
            return -1

        # find the first station that satisfies solution
        tank = 0
        start = 0
        for i in range(len(gas)):
            # calculate gas left after attempting to reach next station
            tank += gas[i] - cost[i]
            # if next station is unreachable, start over from next station
            if tank < 0:
                start = i+1
                tank = 0

        # return start station once end of array is reached
        return start


class testcase1:
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

class testcase2:
    gas = [2, 3, 4]
    cost = [3, 4, 3]