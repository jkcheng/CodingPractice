# 994. Rotting Oranges
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

from typing import List, Optional

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        def bfs(m, n, fresh_count):
            if grid[m][n] == 2:
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dm, dn in dirs:
                    if (m + dm < 0) or (n + dn < 0) or (m + dm >= rows) or (n + dn >= cols):
                        continue

                    if grid[m + dm][n + dn] == 1:
                        queue.append((m + dm, n + dn))
                        grid[m + dm][n + dn] = 2
                        fresh_count -= 1
            return fresh_count

        fresh_count = 0
        for m in range(rows):
            for n in range(cols):
                if grid[m][n] == 2:
                    queue.append((m, n))
                if grid[m][n] == 1:
                    fresh_count += 1

        cur_minute = 0
        while len(queue) > 0:
            cur_minute += 1
            for _ in range(len(queue)):
                m, n = queue.popleft()
                fresh_count = bfs(m, n, fresh_count)

        return -1 if (fresh_count > 0) else max(cur_minute - 1, 0)

from collections import deque
class mySolution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # O(n), BFS, update adjacent orange status at each step, return number of steps for all the rot

        queue = deque([])  # use deque for optimum

        # add initial rotted to queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        # BFS
        minute = 0
        while len(queue) > 0:
            # iterate through current rotted
            for _ in range(len(queue)):
                orange = queue.popleft()
                i = orange[0]
                j = orange[1]
                # update adjacent oranges and add to queue
                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for di, dj in neighbors:
                    if i + di >= 0 and j + dj >= 0 and i + di < len(grid) and j + dj < len(grid[0]):
                        if grid[i + di][j + dj] == 1:
                            grid[i + di][j + dj] = 2
                            queue.append((i + di, j + dj))

            # update minute
            minute += 1

        # check if any non-rotted left
        fresh = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh = True

        return max(minute - 1, 0) if not fresh else -1


class testcase1:
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    output = 4

class testcase2:
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    output = -1

class testcase3:
    grid = [[0, 2]]
    output = 0

class testcase4:
    grid = [[0]]
    output = 0


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.orangesRotting(testcase1.grid)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.orangesRotting(testcase2.grid)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.orangesRotting(testcase3.grid)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.orangesRotting(testcase4.grid)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")