# 547. Number of Provinces
# Medium
# Topics
# premium lock icon
# Companies
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.
#
#
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
#

from typing import List, Optional

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        return


from collections import deque
class mySolution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # O(n), BFS, start at city 1 and repeatedly add all connected cities to queue
        # mark cities as explored and increment province when queue empties
        # return province count when all cities explored

        queue = deque()
        provinces = 0
        seen = set()


        for i in range(len(isConnected)):
            if i not in seen:
                seen.add(i)
                queue.append(isConnected[i])
                provinces += 1

                # explore all connections
                while len(queue) > 0:
                    for _ in range(len(queue)):
                        connections = queue.popleft()
                        for city,connection in enumerate(connections):
                            if city not in seen and connection == 1:
                                queue.append(isConnected[city])
                                seen.add(city)

        return provinces


class testcase1:
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    output = 2

class testcase2:
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    output = 3


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.findCircleNum(testcase1.isConnected)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.findCircleNum(testcase2.isConnected)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")