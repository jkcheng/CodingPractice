# 200. Number of Islands
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            # check for in-bounds
            if (i < 0) or (j < 0) or (i >= m) or (j >= n):
                return

            # check if explored or water
            if (grid[i][j] == '0') or (grid[i][j] == '-1'):
                return

            # mark as explored
            grid[i][j] = '-1'

            # recursively explore neighbors
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in dirs:
                dfs(i + di, j + dj)

        # iterate through each position and explore
        islandcount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islandcount += 1
                    dfs(i, j)

        return islandcount


class mySolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS, 2D grid
        # start at each cell, explore neighbors recursively until no more land
        # move to next cell and repeat, skip if already explored previously

        m = len(grid)
        n = len(grid[0])

        def explore(grid, i, j):
            # skip exploring if out of bounds
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            # explore neighbors if land
            if grid[i][j] == "1":
                # mark current spot as explored
                grid[i][j] = "X"
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for d1, d2 in directions:
                    explore(grid, i + d1, j + d2)

            return

        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    explore(grid, i, j)
                    num_islands += 1

        return num_islands


class testcase1:
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    output = 1

class testcase2:
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    output = 3

class testcase3:
    grid = [
      ["1","1","1"],
      ["0","1","0"],
      ["1","1","1"]
    ]
    output = 1

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.numIslands(testcase1.grid)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.numIslands(testcase2.grid)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.numIslands(testcase3.grid)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )